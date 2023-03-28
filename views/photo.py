from flask_restx import Resource, Namespace
from container import photo_services
from flask import request
from helpers.decorators import auth_required
from dao.model.photo import PhotoSchema

photo_ns = Namespace('photo')

photo_schema = PhotoSchema()
photos_schema = PhotoSchema(many=True)


@photo_ns.route('/')
class PhotosView(Resource):
    # @auth_required
    def get(self):
        all_photos = photo_services.get_all()
        return photos_schema.dump(all_photos), 200

    # @auth_required
    def post(self):
        req_json = request.json
        photo_services.create(req_json)
        return "Created", 201


@photo_ns.route('/<int:pid>')
class PhotoView(Resource):
    # @auth_required
    def get(self, pid):
        photo = photo_services.get_one(pid)
        return photo_schema.dump(photo), 200

    # @auth_required
    def put(self, pid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = pid
        photo_services.update(req_json)
        return "Updated", 204

    # @auth_required
    def patch(self, pid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = pid
        photo_services.update(req_json)
        return "Updated partial", 204

    # @auth_required
    def delete(self, pid):
        photo_services.delete(pid)
        return "Deleted", 204
