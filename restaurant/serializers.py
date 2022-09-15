from ninja import Schema, ModelSchema
from .models import Restaurant

class RestaurantIn(Schema):
    name: str
    restaurant_type: str
    rating: int = None

class RestaurantOut(Schema):
    name: str
    restaurant_type: str
    rating: int

class Message(Schema):
    message: str
