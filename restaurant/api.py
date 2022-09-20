from ninja import Router

from menu.models import Ingredient, Dish
from .models import Restaurant
from .serializers import RestaurantIn, RestaurantOut, Message
from menu.serializers import DishIn, DishOut, IngredientIn, IngredientOut
from typing import List
from django.shortcuts import get_object_or_404


router = Router()

@router.post("/", response={200: Message, 400: None})
def create_restaurant(request, payload: RestaurantIn):
    restaurant = Restaurant(**payload.dict())
    restaurant.save()
    return 200, { "message": "Successfully Created" }

@router.get("/", response=List[RestaurantOut])
def list(request, search_query: str = ""):
    if search_query:
        restaurant = Restaurant.objects.filter(search_terms__icontains=search_query)
        return restaurant
    else:
        return Restaurant.objects.all()

@router.get('/{restaurant_id}/', response=RestaurantOut)
def get_restaurant(request, restaurant_id: int):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    return restaurant

@router.put('/{restaurant_id}/', response=RestaurantIn)
def update_restaurant(request, payload: RestaurantIn, restaurant_id: int):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    for attribute, value in payload.dict().items():
        setattr(restaurant, attribute, value)
    restaurant.save()
    return restaurant

@router.delete('/{restaurant_id}/', response={200: Message, 400: None})
def delete_restaurant(request, restaurant_id: int):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    restaurant.delete()
    return 200, { "message": "Delete Successfull"}

@router.get('/{restaurant_id}/menu', response=List[DishOut])
def get_menu(request, restaurant_id: int):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    menu = restaurant.menu.dish_set.all()
    return menu

@router.get('/{restaurant_id}/menu/{dish_id}/', response=DishOut)
def get_dish(request, dish_id: int):
    dish = get_object_or_404(Dish, id=dish_id)
    return dish

@router.get('/{restaurant_id}/menu/{dish_id}/ingredients', response=List[IngredientOut])
def get_dish_ingredients(request, dish_id: int):
    dish = get_object_or_404(Dish, id=dish_id)
    ingredients = dish.ingredient_set.all()
    return ingredients

@router.post("/{restaurant_id}/menu/", response={200: Message, 400: None})
def add_dish_to_menu(request, restaurant_id: int, payload: DishIn):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    restaurant.menu.dish_set.add(Dish.objects.create(**payload.dict(), menu=restaurant.menu))
    restaurant.save()
    return 200, { "message": "Dish Added" }

@router.post("/{restaurant_id}/menu/{dish_id}/", response={200: Message, 400: None})
def add_ingredient_to_dish(request, restaurant_id: int, dish_id:int, payload: IngredientIn):
    dish = get_object_or_404(Dish, id=dish_id)
    dish.ingredient_set.add(Ingredient.objects.create(**payload.dict()))
    dish.save()
    return 200, { "message": "Ingredient Added" }
