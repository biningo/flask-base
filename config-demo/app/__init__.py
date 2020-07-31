from flask import Flask

import seetings


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(seetings.envs.get(env))
    return app