from ninja import Schema, ModelSchema


class RestaurantIn(Schema):
    name: str
    restaurant_type: str
    rating: int = None

class RestaurantOut(Schema):
    id: int
    name: str
    restaurant_type: str
    rating: int

class Message(Schema):
    message: str
