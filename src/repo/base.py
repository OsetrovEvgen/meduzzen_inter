from db.base import Session


class BaseRepository:
    def __init__(self, session: Session):
        self.session = session
