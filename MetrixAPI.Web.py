from flask import Flask, request
from flask_restful import Resource, Api
import simplejson
import MetrixApiCore as core

db_connect = core.__database__
app = Flask(__name__)
api = Api(app)

class Article_By_ID(Resource):
   def get(self, article_id):
      try:
         return core.get_article_by_id(article_id)
      except Exception as e:
         print(e)

class Article_By_Category(Resource):
   def get(self, category):
      try:
         return core.get_articles_by_category(category)
      except Exception as e:
         print(e)

api.add_resource(Article_By_ID, '/articles/id/<article_id>') #get all article data by id
api.add_resource(Article_By_Category, '/articles/category/<category>')

if __name__ == "__main__":
    app.run(port='5002')