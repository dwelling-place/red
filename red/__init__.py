from flask import Flask

__all__ = 'create_app',

def create_app():
	application = Flask('red', instance_relative_config=True)
	application.config.from_pyfile('application.cfg', silent=True)

	from .routes import blueprint, mongo, api

	application.register_blueprint(blueprint)
	mongo.init_app(application)
	api.init_app(application)

	return application
