import jwt

from flask import request, abort
from constants import JWT_ALGORITHM, JWT_SECRET


def auth_required(func):
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]

        try:
            jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except Exception:
            abort(401)

        return func(*args, **kwargs)

    return wrapper
