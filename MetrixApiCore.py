
from flask_jsonpify import jsonpify
import DataHandler 

def get_article_by_id(article_id):
  try:
    cur = DataHandler.Build_Cursor(f"SELECT * FROM Articles WHERE ID = %s", (article_id))     
    return DataHandler.mysql_cursor_to_json(cur)
  except Exception as e:
    print(e)
  finally:
    cur.close() 

def get_articles_by_category(category):
  try:
      cur = DataHandler.build_cursor(f"SELECT * FROM Articles WHERE category = %s", (category))  
      return DataHandler.mysql_cursor_to_json(cur)
  except Exception as e:
    print(e)
  finally:
    cur.close() 

def get_articles_by_canidate(canidate):
  try:
      cur = DataHandler.Build_Cursor(f"SELECT * FROM Articles WHERE Canidate=%s", (canidate))
      return DataHandler.mysql_cursor_to_json(cur)
  except Exception as eL
    print(e)
  finally:
  cur.close()

def get_canidate_info(canidate):
  try:
      cur = DataHandler.Build_Cursor(f"SELECT * FROM Canidates WHERE Canidate=%s", (canidate))
      return DataHandler.mysql_cursor_to_json(cur)
  except Exception as eL
    print(e)
  finally:
  cur.close()

