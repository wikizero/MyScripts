# coding:utf-8
import pandas as pd
from sqlalchemy import create_engine
import sys
import getopt


def input_handle():
	output, connection, out_type, db_engine, sql = '', '', 'json', 'mysql', ''
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'hi:o:c:t:e:s:')
	except getopt.GetoptError, e:
		print 'forMySQL.py -c <user:pw@host:port/db> -o <output> -s <sql>'
		print e
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'forMySQL.py -c <user:pw@host:port/db> -o <output> -s <sql>'
			sys.exit()
		elif opt in ('-o', '--output'):
			output = arg
		elif opt in ('-c', '--connect'):
			connection = arg
		elif opt in ('-t', '--type'):
			out_type = arg
		elif opt in ('-e', '--engine'):
			db_engine = arg
		elif opt in ('-s', '--sql'):
			sql = arg
	return connection, output, out_type, db_engine, sql


def main():
	connect, output, out_type, db_engine, sql = input_handle()
	connect_info = db_engine + '://' + connect  # 'mysql://root:root@39.108.141.110:3306/world'
	engine = create_engine(connect_info, encoding='utf-8')

	tables = engine.table_names()

	if sql:
		df = pd.read_sql_query(sql, engine)
		print 'processing...'
		df.to_json(output, orient='records')

	else:
		for table in tables:
			sql = 'select * from ' + table
			df = pd.read_sql_query(sql, engine)
			print 'processing...'
			df.to_json(table + '.json', orient='records')


if __name__ == '__main__':
	main()
