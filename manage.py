#!env/bin/python

import os

from flask_script import Manager, Server
from wsgi_basic_auth import BasicAuth

from red import create_app


def find_assets():
    """Yield paths for all static files and templates."""
    for name in ['static', 'templates']:
        directory = os.path.join(app.config['PATH'], name)
        for entry in os.scandir(directory):
            if entry.is_file():
                yield entry.path

application = create_app()

os.environ['WSGI_AUTH_CREDENTIALS'] = application.config.WSGI_AUTH_CREDENTIALS

application.wsgi_app = BasicAuth(application.wsgi_app)

server = Server(host='0.0.0.0', extra_files=find_assets())

manager = Manager(application)
manager.add_command('run', server)


if __name__ == '__main__':
    manager.run()