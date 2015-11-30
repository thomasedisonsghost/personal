"""
A lot of the time we just want to very simply wrap a blueprint in a full app for the sake of convenience.
"""
from flask import Flask, request, session, abort, url_for

import random, string

def random_string(num=20):
    return ''.join(random.choice(string.letters) for i in range(num))



def make_app(blueprint, csrf_protect=True, facebook=False):

    app = Flask(str(id(blueprint)))

    app.config["MONGODB_SETTINGS"] = {"DB": "blog"}
    app.config["SECRET_KEY"] = "indico"
    app.config['DEBUG'] = True
    app.jinja_env.autoescape = False

    app.register_blueprint(blueprint)
    if csrf_protect:
        app = protect(app)
    return app


def protect(app, secret_key=random_string()):

    app.config['SECRET_KEY'] = secret_key

    @app.before_request
    def csrf_protect():
        if request.method == "POST":
            token = session.pop('_csrf_token', None)
            if not token or token != request.form.get('_csrf_token'):
                abort(403)

    def generate_csrf_token():
        if '_csrf_token' not in session:
            session['_csrf_token'] = random_string(100)
        return session['_csrf_token']

    app.jinja_env.globals['csrf_token'] = generate_csrf_token
    return app
