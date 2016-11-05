from flask import Flask

__all__ = 'application',

application = Flask('red', instance_relative_config=True)
application.config.from_object('red.default_settings')
application.config.from_pyfile('application.cfg', silent=True)

# Just get these imported
from .routes import *
