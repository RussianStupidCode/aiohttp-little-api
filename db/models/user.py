import hashlib
from db.data_base import data_base as db
from db import config


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))

    def __str__(self):
        return f'<User {self.username}>'

    @classmethod
    def set_password(self, raw_password: str):
        raw_password = f'{raw_password}{config.SALT}'
        return hashlib.md5(raw_password.encode()).hexdigest()

    def check_password(self, raw_password: str):
        raw_password = f'{raw_password}{config.SALT}'
        return self.password == hashlib.md5(raw_password.encode()).hexdigest()

