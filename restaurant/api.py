from ninja import Router
from .models import Restaurant
from .serializers import RestaurantIn, RestaurantOut, Message
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
