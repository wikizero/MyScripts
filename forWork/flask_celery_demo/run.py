from project.MyScripts.forWork.flask_celery_demo import create_app
from gevent.pywsgi import WSGIServer

app = create_app()


http_server = WSGIServer(('localhost', 8080), app)
http_server.serve_forever()

# https://github.com/miguelgrinberg/flasky-with-celery  最佳实践demo
