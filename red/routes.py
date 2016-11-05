from . import application
from flask_restful import Resource, Api

@application.route('/')
def index():
	...

api = Api(application)

class Project(Resource):
	def get(self, projid):
		return {'hello': 'world'}

	def put(self, projid):
		...

	def delete(self, projid):
		...

api.add_resource(Project, '/projects/<string:projid>')


class ProjectList(Resource):
	def get(self):
		...

	def post(self):
		...

api.add_resource(ProjectList, '/projects')
