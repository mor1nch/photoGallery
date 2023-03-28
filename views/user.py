from flask_restx import Resource, Namespace
from container import user_services
from flask import request
from helpers.decorators import auth_required
from dao.model.user import UserSchema

user_ns = Namespace('user')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UsersView(Resource):
    # @auth_required
    def get(self):
        all_users = user_services.get_all()
        return users_schema.dump(all_users), 200

    # @auth_required
    def post(self):
        req_json = request.json
        user_services.create(req_json)
        return "Created", 201


@user_ns.route('/<int:uid>')
class UserView(Resource):
    # @auth_required
    def get(self, uid):
        user = user_services.get_one(uid)
        return user_schema.dump(user), 200

    # @auth_required
    def put(self, uid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        user_services.update(req_json)
        return "Updated", 204

    # @auth_required
    def patch(self, uid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        user_services.update(req_json)
        return "Updated partial", 204

    # @auth_required
    def delete(self, uid):
        user_services.delete(uid)
        return "Deleted", 204
