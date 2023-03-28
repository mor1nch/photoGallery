from dao.photo import PhotoDAO
from dao.user import UserDAO

from services.auth import AuthService
from services.photo import PhotoService
from services.user import UserService

from setup_db import db

photo_dao = PhotoDAO(session=db.session)
photo_services = PhotoService(dao=photo_dao)

user_dao = UserDAO(db.session)
user_services = UserService(user_dao)

auth_services = AuthService(user_services)
