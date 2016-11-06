#!env/bin/python

import os

from flask_script import Manager, Server
from wsgi_basic_auth import BasicAuth

from red import create_app
from red.settings import get_config


def find_assets(app):
    """Yield paths for all static files and templates."""
    for name in ['static', 'templates']:
        directory = os.path.join(app.config['PATH'], name)
        for entry in os.scandir(directory):
            if entry.is_file():
                yield entry.path


config = get_config(os.getenv('FLASK_ENV'))
os.environ['WSGI_AUTH_CREDENTIALS'] = config.WSGI_AUTH_CREDENTIALS

application = create_app(config)
application.wsgi_app = BasicAuth(application.wsgi_app)

server = Server(host='0.0.0.0', extra_files=find_assets(application))

manager = Manager(application)
manager.add_command('run', server)


if __name__ == '__main__':
    manager.run()
