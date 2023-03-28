from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.photo import photo_ns
from views.user import user_ns
from dao.model.photo import Photo
from dao.model.user import User


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app=app, title="photoGallery", doc="/docs")
    api.add_namespace(photo_ns)
    api.add_namespace(user_ns)

    # create_data(app, db)


def create_data(app, db):
    with app.app_context():
        db.create_all()
        u1 = User(first_name="Vasya", surname="Petrov", phone="79111234567", password="my_little_pony")
        u2 = User(first_name="Oleg", surname="Mihaylov", phone="79456713425", password="qwerty")
        u3 = User(first_name="Petya", surname="Dubov", phone="79845381473", password="P@ssw0rd")

        p1 = Photo(name="picture1", url="https://akspic.ru/image/171455-zhivopis-illustracia-art-voda-oblako",
                   owner_id=1)
        p2 = Photo(name="picture2",
                   url="https://akspic.ru/image/171545-graficheskij_dizajner-rabochij_process-dizajn-grafika-dizajner",
                   owner_id=2)
        p3 = Photo(name="picture3", url="https://akspic.ru/image/171330-voda-priroda-zemlya-derevo-vodoem", owner_id=3)

        with db.session.begin():
            db.session.add_all([p1, p2, p3])
            db.session.add_all([u1, u2, u3])


app = create_app(Config())

if __name__ == '__main__':
    app.run()
