import time
from datetime import datetime
from project.MyScripts.forWork.flask_celery_demo.celery_worker import celery


@celery.task
def send_email(num):
    for i in range(num):
        time.sleep(1)
        print(i)

    print(datetime.now())