from database import db
import datetime

class Ritual(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=False)
    create_date = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    occupation = db.Column(db.String(120))
    location = db.Column(db.String(200))
    gender = db.Column(db.String(1))
    ritual_text = db.Column(db.Text)

    def __init__(self, name, email, occupation, location, gender, ritual_text):
        self.name = name
        self.email = email
        self.create_date = datetime.datetime.utcnow()
        self.occupation = occupation
        self.location = location
        self.gender = gender
        self.ritual_text = ritual_text

    def __repr__(self):
        return '<User %r>' % self.email

    def save(self):
        db.session.add(self)

    def get_all(self):
        db.get_all()