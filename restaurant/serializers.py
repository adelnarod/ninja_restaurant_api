from ninja import Schema, ModelSchema
from .models import Restaurant

class RestaurantIn(Schema):
    name: str
    restaurant_type: str
    rating: int = None
