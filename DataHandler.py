import mysql.connector
import Authentication
import Utilities
import json 

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

   rslt = json.dumps(json_data, cls=Utilities.CustomJsonEncoder)
   print(rslt)
   return rslt

def Build_Cursor(query, parameters):
  cur = __database__.cursor(buffered = true)
  return cur.execute(query, parameters)