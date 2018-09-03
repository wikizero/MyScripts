from flask import Flask, request
from gevent.pywsgi import WSGIServer
from movie import movie_bp

import time
from datetime import datetime

app = Flask(__name__)
app.register_blueprint(movie_bp, url_prefix='/movie')


@app.route('/', methods=['GET'])
def test_asyn_one():
    for i in range(10):
        time.sleep(1)
        print(i)

    print(datetime.now())
    return 'hello asyc'


if __name__ == "__main__":
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()

    # or
    # app.run(threaded=True)

    # https://blog.csdn.net/dutsoft/article/details/51452598
    # 配置文件启动

    # TODO 启动方式 : gunicorn -w 4 -b 127.0.0.1:5000 flask_asyc_2:app

