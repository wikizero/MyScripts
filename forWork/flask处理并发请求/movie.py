from flask import Blueprint
import time
from datetime import datetime

movie_bp = Blueprint("movie", __name__)


@movie_bp.route("/")
def movie():
    for i in range(10):
        time.sleep(1)
        print(i)

    print(datetime.now())
    return "movie"
