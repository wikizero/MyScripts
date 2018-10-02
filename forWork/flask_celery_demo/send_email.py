from flask import Blueprint
from project.MyScripts.forWork.flask_celery_demo.async_task import send_email

email_bp = Blueprint("email", __name__)


@email_bp.route("/tasks/<int: num>")
def email(num: int):
    send_email.delay(num)
    return "success"
