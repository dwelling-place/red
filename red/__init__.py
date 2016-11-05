from flask import Flask

__all__ = 'create_app',

application = Flask('red', instance_relative_config=True)
application.config.from_pyfile('application.cfg', silent=True)

# Just get these imported
from .routes import *
