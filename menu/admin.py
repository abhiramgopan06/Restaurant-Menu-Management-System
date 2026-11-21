from django.contrib import admin
from .models import FoodItem


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "availability", "created_at")
    list_filter = ("category", "availability")
    search_fields = ("name", "description")
