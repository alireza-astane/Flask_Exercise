#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    "db": "your_database",
    "host": "127.0.0.1",
    "port": 27017,
}
db = MongoEngine()
db.init_app(app)


class User(db.Document):
    name = db.StringField()
    email = db.StringField()

    def to_json(self):
        return {"name": self.name, "email": self.email}


user = User(name="ali", email="a.com")
user.save()
for user in User.objects():
    print(user.to_json())


@app.route("/", methods=["GET"])
def query_records():
    name = request.args.get("name")
    user = User.objects(name=name).first()
    if not user:
        return jsonify({"error": "data not found"})
    else:
        return jsonify(user.to_json())


@app.route("/", methods=["PUT"])
def create_record():
    print("hi 0", request.data)

    record = json.loads(request.data)
    print("hi 1 ", record)
    user = User(name=record["name"], email=record["email"])
    print("hi 2 ", user)
    user.save()
    print("saved")
    return jsonify(user.to_json())


@app.route("/", methods=["POST"])
def update_record():
    record = json.loads(request.data)
    user = User.objects(name=record["name"]).first()
    if not user:
        return jsonify({"error": "data not found"})
    else:
        user.update(email=record["email"])
    return jsonify(user.to_json())


@app.route("/", methods=["DELETE"])
def delete_record():
    record = json.loads(request.data)
    user = User.objects(name=record["name"]).first()
    if not user:
        return jsonify({"error": "data not found"})
    else:
        user.delete()
    return jsonify(user.to_json())


if __name__ == "__main__":
    app.run(debug=True)
