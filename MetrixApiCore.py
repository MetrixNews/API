import mysql.connector
import Authentication
from flask_jsonpify import jsonpify
import json 
from decimal import Decimal

__database__ = mysql.connector.connect(
    host        = Authentication.SQL_HOST,
    user        = Authentication.SQL_USERNAME,
    password    = Authentication.SQL_PASSWORD,
    database    = "Metrix"
)

def mysql_cursor_to_json(cur):
   row_headers=[x[0] for x in cur.description]
   rv = cur.fetchall()
   json_data=[]
   for result in rv:
      json_data.append(dict(zip(row_headers, result)))

   rslt = json.dumps(json_data, cls=CustomJsonEncoder)
   print(rslt)
   return rslt

def get_article_by_id(article_id):
   try:
      cur = __database__.cursor(buffered=True)
      query = cur.execute(f"SELECT * FROM Articles WHERE ID = {article_id}")       
      return mysql_cursor_to_json(cur)
   except Exception as e:
      print(e)
   finally:
      cur.close() 


def get_articles_by_category(category):
   try:
         cur = __database__.cursor(buffered=True)
         query = cur.execute(f"SELECT * FROM Articles WHERE category = '{article_id}''")       
         return mysql_cursor_to_json(cur)
   except Exception as e:
      print(e)
   finally:
      cur.close() 

class CustomJsonEncoder(json.JSONEncoder):
   def default(self, obj):
      if isinstance(obj, Decimal):
         return float(obj)
      return super(CustomJsonEncoder, self).default(obj)