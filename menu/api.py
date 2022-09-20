from ninja import Router
from .models import Dish, Ingredient
from .serializers import IngredientIn, Message


router = Router()

@router.post('/ingredients/', response={200: Message, 400: None})
def create_ingredient(request, payload: IngredientIn):
    ingredient = Ingredient(**payload.dict())
    ingredient.save()
    return 200, { "message": "Successfully Created" }
