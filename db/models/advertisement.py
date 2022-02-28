from db.data_base import data_base as db
from db.models.user import User
from datetime import datetime


class Advertisement(db.Model):
    __tablename__ = "advertisments"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    text = db.Column(db.Text)
    publish_date = db.Column(db.DateTime, default=datetime.utcnow)
    owner_id = db.Column(db.Integer, db.ForeignKey(User.id))

    def __str__(self):
        return f'<Title: {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'owner_id': self.owner_id,
            "title": self.title,
            "text": self.text,
            "publish_date": str(self.publish_date)
        }