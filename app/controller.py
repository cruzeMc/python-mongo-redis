from flask import jsonify, render_template
from flask_restful import Api, Resource

from app.service.mongo_service import *
from app.service.university_service import *
from app.service.user_service import *

api = Api(app)
app.config.from_object(CacheConfig)
cache = Cache(app)


@app.route('/index')
def index():
    user = {'username': 'Cruze'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


class UserController(Resource):
    def get(self, username):
        user = get_user2(username)
        if not user:
            404
        else:
            return jsonify(user.dump(user))


class UniversityController(Resource):
    def get(self):
        country = request.args.get('country')
        response = get_university(country)
        return jsonify(response.json())


class Mongo(Resource):
    def get(self, id):
        return get_person(id=id)

    def post(self, id):
        person = request.get_json();
        result = create_person(person)
        return {'_id': result.inserted_id, 'inserted': result.acknowledged}

    def put(self, id):
        person = request.get_json();
        result = update_person(id, person)
        return {'_id': id}, 200


class MongoList(Resource):
    def get(self, age):
        return get_persons(age=age)


class MongoDBSetup(Resource):
    def get(self):
        database_update()


api.add_resource(UserController, '/user/<username>')
api.add_resource(UniversityController, '/universities')
api.add_resource(Mongo, '/mongo/id/<int:id>')
api.add_resource(MongoList, '/mongo/age/<int:age>')
api.add_resource(MongoDBSetup, '/db_setup')
