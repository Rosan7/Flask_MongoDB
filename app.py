from flask import Flask,request,jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient
import json
from bson import json_util
from flask_restful import Resource,Api
app = Flask(__name__)
api = Api(app)
# we have created a new database in mongodb named as myDB and a new collection named user_list
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDB"
mongodb_client = PyMongo(app)
db = mongodb_client.db

# @app.route("/get_all_users", methods=["GET"])
class GetUsers(Resource):
    def get(self):
        doc_list = list(db.user_list.find())
        return json.loads(json_util.dumps(doc_list))
class GetUsersWithId(Resource):
    def get(self,id):
        doc_list = list(db.user_list.find({"id": id}))
        req_user = doc_list[0]
        return json.loads(json_util.dumps(req_user))
    
class AddUser(Resource):
    def post(self):
        user_details = request.get_json()
        data = dict()
        data["id"] = user_details["id"]
        data["name"] = user_details["name"]
        data["email"] = user_details["email"]
        data["password"] = user_details["password"]
        db.user_list.insert_one(data)
        return jsonify(msg="User Added Successfully")
class UpdateDb(Resource):
    def put(self, id):
        data = request.get_json()
        for key,value in data.items():
            value = {"$set": {key: value}}
            q = {"id":id}
            db.user_list.update_one(q,value)
        return jsonify(msg="User Updated Successfully")
    def delete(self,id):
        doc_list = list(db.user_list.find({"id": id}))
        doc = doc_list[0]
        db.user_list.delete_one(doc)
        return jsonify(msg="User deleted successfully")
        
# def get_all_users():
#     '''This function returns all the user infomation which are stored in the database in form of documents
#     The function returns a list which contains list of json objects which has user information'''
    
#     doc_list = list(db.user_list.find())
#     return json.loads(json_util.dumps(doc_list))
# @app.route("/get_users_with/<int:id>", methods=["GET"])
# def get_users_with(id):
#     ''' This function returns the info of a specific user with the given id in form of a json object'''

#     doc_list = list(db.user_list.find({"id": id}))
#     req_user = doc_list[0]
#     return json.loads(json_util.dumps(req_user))
# @app.route("/add_user",methods=["POST"])
# def add_user():
#     '''This adds the user information in form of document to the collection'''

#     user_details = request.get_json()
#     data = dict()
#     data["id"] = user_details["id"]
#     data["name"] = user_details["name"]
#     data["email"] = user_details["email"]
#     data["password"] = user_details["password"]
#     db.user_list.insert_one(data)
#     return jsonify(msg="User Added Successfully")
# @app.route("/update_user_with_id/<int:id>",methods=["PUT"])
# def update_user_with_id(id):
#     '''This updates the information of the user with the specified id'''

#     data = request.get_json()
#     for key,value in data.items():
#         value = {"$set": {key: value}}
#         q = {"id":id}
#         db.user_list.update_one(q,value)
#     return jsonify(msg="User Updated Successfully")
# @app.route("/delete_user/<int:id>",methods=["DELETE"])
# def delete_user(id):
#     '''This method deletes the user with the specific id'''

#     doc_list = list(db.user_list.find({"id": id}))
#     doc = doc_list[0]
#     db.user_list.delete_one(doc)
#     return jsonify(msg="User deleted successfully")
api.add_resource(GetUsers,'/get_all_users')
api.add_resource(GetUsersWithId,'/get_users_with_id/<int:id>')
api.add_resource(AddUser,"/add_user")
api.add_resource(UpdateDb,"/update_db/<int:id>")
                    
if __name__ == "__main__":
    
    app.run(host="0.0.0.0",port="5000", debug=True)
