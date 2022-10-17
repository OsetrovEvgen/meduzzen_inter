from databases import Database


class BaseRepository:
    def __int__(self, database: Database):
        self.database = database
