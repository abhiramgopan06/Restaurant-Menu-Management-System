from django.urls import path
from . import views

urlpatterns = [
    path("", views.food_item_list, name="food_item_list"),
    path("food/add/", views.add_food_item, name="add_food_item"),
    path("food/<int:item_id>/edit/", views.edit_food_item, name="edit_food_item"),
    path("food/<int:item_id>/delete/", views.delete_food_item, name="delete_food_item"),
    path("food/<int:item_id>/toggle-availability/", views.toggle_food_availability, name="toggle_food_availability"),
]
