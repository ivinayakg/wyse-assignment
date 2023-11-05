from pymongo import MongoClient
from django.conf import settings
import jwt

def get_db_handle(db_name, connection_string):
    client = MongoClient(connection_string)
    db_handle = client[db_name]
    return db_handle, client

db, mongoClient = get_db_handle(settings.DB_NAME, settings.DB_CONNECT_URL)

class JWTUtils:
    @classmethod
    def create_token(self, data):
        return jwt.encode(data, settings.SECRET_KEY, "HS256")
    
    @classmethod
    def verify(self, token):
        return jwt.decode(token, settings.SECRET_KEY, ["HS256"])