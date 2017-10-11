# coding:utf-8
import MySQLdb
import re
import pandas as pd


class MySQLHelper:
	def __init__(self):
		pass

	@staticmethod
	def create_engine(connect, charset='utf8'):
		user, password, host, port, db_name = re.split(r':|@|/', connect)
		db_connect = MySQLdb.connect(user=user, host=host, passwd=password, db=db_name, charset=charset)
		return db_name, db_connect, db_connect.cursor()

	@staticmethod
	def source_analysis(source):
		if isinstance(source, list):
			return source
		elif isinstance(source, pd.DataFrame):
			return source.to_dict(orient='records')
		else:
			raise Exception('Data type is not supported')

	@staticmethod
	def insert_many(table, source, engine, conflict=None, limit=10000, field_status=None):
		db_name, con, cur = engine

		if conflict == 'replace':
			prefix = 'replace into ' + table
		elif conflict == 'ignore':
			prefix = 'insert ignore into ' + table
		elif not conflict:
			prefix = 'insert into ' + table
		else:
			raise Exception('conflict is not supported, It just can be replace or ignore')

		source = MySQLHelper.source_analysis(source)
		fields = source[0].keys()
		values = [one.values() for one in source]

		if field_status:
			fields = map(field_status, fields)

		fields_str = ' (' + ','.join(fields) + ') '
		values_str = ' (' + ','.join(['%s']*len(fields)) + ') '

		sql = prefix + fields_str + 'values' + values_str

		print sql

		for index in xrange(0, len(values), limit):
			insert_values = values[index:index+limit]
			cur.executemany(sql, insert_values)
			con.commit()
			print sql
			print len(insert_values), ' rows affected'

		return True

if __name__ == '__main__':
	# how to use it in your work
	source = [
		{
			'name': 'Alice',
			'age': 19
		},
		{
			'name': 'Tom',
			'age': 18
		}
	]
	engine = MySQLHelper.create_engine('root:password@127.0.0.1:3306/test')
	MySQLHelper.insert_many('student', source, engine, conflict='replace')