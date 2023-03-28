from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid: int) -> list[User]:
        return self.session.query(User).get(uid)

    def get_all(self) -> list[User]:
        return self.session.query(User).all()

    def create(self, user_data: dict) -> dict:
        new_user = User(**user_data)

        self.session.add(new_user)
        self.session.commit()
        return new_user

    def update(self, user_data: dict) -> None:
        user = self.get_one(user_data.get("id"))

        if 'first_name' in user:
            user.name = user_data.get("first_name")
        if 'surname' in user:
            user.url = user_data.get("surname")
        if 'phone' in user:
            user.owner_id = user_data.get("phone")
        if 'password' in user:
            user.owner_id = user_data.get("password")

        self.session.add(user)
        self.session.commit()

    def delete(self, uid: int) -> None:
        user = self.get_one(uid)

        self.session.delete(user)
        self.session.commit()
