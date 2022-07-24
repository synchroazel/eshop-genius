from flask_login import UserMixin
from sqlalchemy.sql import func

from webapp import db


class Wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    db.UniqueConstraint(content, user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150))
    password = db.Column(db.String(150))
    wishlist = db.relationship('Wishlist')
