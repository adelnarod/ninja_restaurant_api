from ninja import Schema

class DishOut(Schema):
    id: int
    name: str

class DishIn(Schema):
    name: str

class IngredientIn(Schema):
    name: str

class IngredientOut(Schema):
    name: str

class Message(Schema):
    message: str
