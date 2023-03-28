from dao.model.photo import Photo


class PhotoDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, pid: int) -> list[Photo]:
        return self.session.query(Photo).get(pid)

    def get_all(self) -> list[Photo]:
        return self.session.query(Photo).all()

    def get_by_owner_id(self, owner_id: int) -> list[Photo]:
        return self.session.query(Photo).filter(Photo.owner_id == owner_id).all()

    def create(self, photo_data: dict) -> dict:
        new_photo = Photo(**photo_data)

        self.session.add(new_photo)
        self.session.commit()
        return new_photo

    def update(self, photo_data: dict) -> None:
        photo = self.get_one(photo_data.get("id"))

        if 'name' in photo:
            photo.name = photo_data.get("name")
        if 'url' in photo:
            photo.url = photo_data.get("url")
        if 'owner_id' in photo:
            photo.owner_id = photo_data.get("owner_id")

        self.session.add(photo)
        self.session.commit()

    def delete(self, pid: int) -> None:
        photo = self.get_one(pid)

        self.session.delete(photo)
        self.session.commit()
