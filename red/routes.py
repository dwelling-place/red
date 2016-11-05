from . import application
from flask_restful import Resource, Api
from flask.ext.pymongo import PyMongo

mongo = PyMongo(application)

@application.route('/')
def index():
    ...

api = Api(application)

class Project(Resource):
    def get(self, projid):
        return mongo.db.projects.find_one_or_404({'_id': projid})

    def put(self, projid):
        mongo.db.projects.replace_one({'_id': projid}, request.form)
        return '', 201

    def delete(self, projid):
        mongo.db.projects.delete_one({'_id': projid})
        return '', 204

api.add_resource(Project, '/projects/<string:projid>')


class ProjectList(Resource):
    def get(self):
        return mongo.db.projects.find()

    def post(self):
        res = mongo.db.projects.insert_one(request.form)
        # FIXME: Created
        return res.inserted_id, 201

api.add_resource(ProjectList, '/projects')
