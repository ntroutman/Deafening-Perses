from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

import database

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
database.configure(app)


# Models have to be imported after the database has been configured
from rituals import Ritual


@app.route('/')
def homepage():
    random_ritual = Ritual.get_all()

    return render_template('index.html', random_ritual=random_ritual)


if __name__ == '__main__':
    app.run()