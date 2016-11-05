from . import application
from flask import render_template, request
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

mongo = PyMongo(application)

@application.route('/')
def index():
    return render_template('index.html')

api = Api(application)

def jsonify_doc(doc):
    return {
        k: str(v) if isinstance(v, ObjectId) else v
        for k,v in doc.items()
    }

class Project(Resource):
    def get(self, projid):
        return jsonify_doc(mongo.db.projects.find_one_or_404({'_id': ObjectId(projid)}))

    def put(self, projid):
        mongo.db.projects.replace_one({'_id': ObjectId(projid)}, request.form.to_dict())
        return '', 204

    def delete(self, projid):
        mongo.db.projects.delete_one({'_id': ObjectId(projid)})
        return '', 204

api.add_resource(Project, '/projects/<projid>')


class ProjectList(Resource):
    def get(self):
        return [
            jsonify_doc(doc)
            for doc in mongo.db.projects.find()
        ]

    def post(self):
        res = mongo.db.projects.insert_one(request.form.to_dict())
        return '', 201, {'Location': api.url_for(Project, projid=res.inserted_id)}

api.add_resource(ProjectList, '/projects')