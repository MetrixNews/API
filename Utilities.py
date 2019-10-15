from decimal import Decimal

class CustomJsonEncoder(json.JSONEncoder):
   def default(self, obj):
      if isinstance(obj, Decimal):
         return float(obj)
      return super(CustomJsonEncoder, self).default(obj)