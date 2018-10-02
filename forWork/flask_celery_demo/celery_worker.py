from project.MyScripts.forWork.flask_celery_demo import create_app
from project.MyScripts.forWork.flask_celery_demo.MakeCelery import make_celery

celery = make_celery(create_app())

