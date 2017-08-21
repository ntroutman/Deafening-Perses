from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
from rituals import Ritual

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def homepage():
    random_ritual = Ritual.get_all()

    return render_template('index.html', random_ritual=random_ritual)


if __name__ == '__main__':
    app.run()