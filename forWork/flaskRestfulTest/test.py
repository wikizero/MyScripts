from flask import Flask, request
from flask_restful import Api, Resource, reqparse
# from django.contrib.auth.decorators import login_required

app = Flask(__name__)
api = Api(app)


def login_required(func):
    """
    decorator for checking user permission
    """

    def decorator(*args, **kwargs):
        user_id = kwargs.get('user_id', False)
        # if not user_id:
        #     return
        if not user_id or user_id != 'xx':
            return {'msg': 'Error'}
        return func(*args, **kwargs)

    return decorator


class UserAPI(Resource):
    def get(self, id):
        print(id)

    def put(self, id):
        pass

    def delete(self, id):
        pass

    @login_required
    def post(self, user_id, id):
        print(user_id, id)
        print(request.json)

        return {'msg': 'success'}


api.add_resource(UserAPI, '/users/<string:user_id>/<int:id>', '/')

if __name__ == '__main__':
    app.run(debug=True)
