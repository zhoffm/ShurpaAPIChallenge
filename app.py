from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

HOST = 'http://localhost:8080'
TOKEN = 'abc123'
EXISTING_EMAIL = 'test@example.com'
EXISTING_ITEM_ID = 'abc123'

data = {}

parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('name')
parser.add_argument('email')


@app.route('/')
def index():
    return "Hello, World!"


class NotFound(Resource):
    def get(self):
        return abort(404)


class ItemNotFound(Resource):
    def get(self):
        return abort(404)

    def post(self):
        return abort(404)


class Collection(Resource):
    def get(self):
        return '', 405

    def post(self):
        args = parser.parse_args()
        try:
            print(request.headers['Authorization'])
        except KeyError:
            pass
        print(request.headers)
        if 'Authorization' not in request.headers:
            return '', 401
        elif args['email'] is not None and EXISTING_EMAIL not in args['email']:
            if '@example.com' in args['email']:
                return '', 201
            elif args['email'] == ' ':
                return '', 400
        else:
            return '', 400


class ExistingItem(Resource):

    def get(self):
        return '', 403

    def post(self):
        return '', 403


class NewItem(Resource):

    ITEM_ID = ''

    def get(self):
        return '', 200

    def post(self):
        return '', 200


api.add_resource(Collection, '/collection')
api.add_resource(ExistingItem, '/item/' + EXISTING_ITEM_ID)
api.add_resource(NewItem, '/item/' + NewItem.ITEM_ID)
api.add_resource(NotFound, '/notfound')
api.add_resource(ItemNotFound, '/item/notfound')

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
