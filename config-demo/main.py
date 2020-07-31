import os
from .app import create_app

if __name__ == '__main__':
    env = os.environ.get('FLASK_ENV','develop')
    app = create_app(env)
    app.run()