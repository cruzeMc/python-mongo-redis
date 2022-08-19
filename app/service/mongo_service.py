from pymongo import MongoClient

from ..config import MongoConfig
from ..model.person import PersonSchema

client = MongoClient(MongoConfig.MONGO_DB_URL, int(MongoConfig.MONGO_DB_PORT))


def database_setup():
    db = client['testdb']
    db.create_collection('myColl')


def database_update():
    db = client['mydb']
    coll = db.get_collection('example')
    coll.delete_many({})

    data = [
        {"_id": 1001, "name": "Ram", "age": 26, "city": "Hyderabad"},
        {"_id": 1002, "name": "Rahim", "age": 27, "city": "Bangalore"},
        {"_id": 1003, "name": "Robert", "age": 28, "city": "Mumbai"},
        {"_id": 1004, "name": "Romeo", "age": 25, "city": "Pune"},
        {"_id": 1005, "name": "Sarmista", "age": 23, "city": "Delhi"},
        {"_id": 1006, "name": "Rasajna", "age": 26, "city": "Chennai"}
    ]

    coll.insert_many(data)


def get_person(id):
    db = client['mydb']
    coll = db.get_collection('example')
    person = coll.find_one({'_id': id})
    person_schema = PersonSchema()
    return person_schema.dump(person)


def get_persons(age):
    db = client['mydb']
    coll = db.get_collection('example')
    persons = []
    for person in coll.find({'age': {'$gte': age}}).sort('age', 1):
        persons.append(person)
    return persons


def create_person(person):
    db = client['mydb']
    coll = db.get_collection('example')
    person_schema = PersonSchema()
    person_schema.load(person)
    return coll.insert_one(person)


def update_person(id, person):
    db = client['mydb']
    coll = db.get_collection('example')

    person_schema = PersonSchema()
    person_schema.load(person)


    coll.update_one({'_id': id}, {'$set':person})


def delete_person(id):
    db = client['mydb']
    coll = db.get_collection('example')
    coll.delete_one({'_id':id})
