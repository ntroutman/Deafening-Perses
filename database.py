from flask_sqlalchemy import SQLAlchemy

db = None

def configure(app):
    global db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/personal_ritual_app'
    db = SQLAlchemy(app)

def create_all():
    db.create_all()

def add(self):
    db.session.add(self)

def commit():
    db.session.commit()

def drop_all():
    db.drop_all()

def get_all():
    db.query.all()