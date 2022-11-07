from app.database import db


class Employeer(db.Model):
    __tablename__= "users"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))