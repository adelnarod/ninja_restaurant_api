from ninja import Router
from .models import Restaurant
from .serializers import RestaurantIn
from typing import List
from django.shortcuts import get_object_or_404

router = Router()

@router.post("/", response=RestaurantIn)
def create_restaurant(request, payload: RestaurantIn):
    restaurant = Restaurant.objects.create(**payload.dict())
    return restaurant

@router.get("/", response=List[RestaurantIn])
def list(request):
    return Restaurant.objects.all()

@router.get('/{restaurant_id}/', response=RestaurantIn)
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

@router.delete('/{restaurant_id}/')
def delete_restaurant(request, restaurant_id: int):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    restaurant.delete()
    return { "successfully_deleted" : True }

@router.get('/search', response=List[RestaurantIn])
def search_restaurant(request, search_query: str):
    restaurant = Restaurant.objects.filter(search_terms__icontains=search_query)
    return restaurant
