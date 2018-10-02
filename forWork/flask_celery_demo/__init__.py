from flask import Flask
from .send_email import email_bp
# from MakeCelery import make_celery


def create_app():
    """
    Create and configure an instance of the Flask application.
    """

    app = Flask(__name__)

    app.config.update(
        CELERY_BROKER_URL='redis://localhost:6379/0',
        CELERY_RESULT_BACKEND='redis://localhost:6379/1'
    )
    # celery = make_celery(app)

    @app.route('/hello')
    def hello():
        return 'Hello, flask!'

    @app.errorhandler(404)
    def page_not_found(e):
        return 'Are you lost?', 404

    @app.errorhandler(500)
    def server_error(e):
        return "We're sorry. Something went wrong. Please try again later. The backend responded with an error!", 500

    # register the database commands
    # init_db()

    # apply the blueprints to the app
    # app.register_blueprint(auth.bp)
    # app.register_blueprint(blog.bp)
    app.register_blueprint(email_bp)

    return app
