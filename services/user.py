import base64
import hashlib
import hmac

from dao.user import UserDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid: int) -> None or list:
        return self.dao.get_one(uid)

    def get_all(self) -> list:
        return self.dao.get_all()

    def create(self, user_data: dict) -> dict:
        user_data["password"] = self.generate_password(user_data["password"])
        return self.dao.create(user_data)

    def update(self, user_data: dict) -> None:
        return self.dao.update(user_data)

    def delete(self, uid: int) -> None:
        self.dao.delete(uid)

    def generate_password(self, password: str):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    def compare_password(self, password_hash, other_password):
        decoded_digest = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            "sha256",
            other_password.encode("utf-8"),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return hmac.compare_digest(decoded_digest, hash_digest)
