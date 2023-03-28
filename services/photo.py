from dao.photo import PhotoDAO


class PhotoService:
    def __init__(self, dao: PhotoDAO):
        self.dao = dao

    def get_one(self, pid: int) -> None or list:
        return self.dao.get_one(pid)

    def get_all(self) -> list:
        return self.dao.get_all()

    def create(self, photo_data: dict) -> dict:
        return self.dao.create(photo_data)

    def update(self, photo_data: dict) -> None:
        return self.dao.update(photo_data)

    def delete(self, pid: int) -> None:
        self.dao.delete(pid)
