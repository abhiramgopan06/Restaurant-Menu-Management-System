from django.core.validators import MinValueValidator
from django.db import models


class FoodItem(models.Model):
    CATEGORY_CHOICES = [
        ("Starters", "Starters"),
        ("Main Course", "Main Course"),
        ("Desserts", "Desserts"),
        ("Beverages", "Beverages"),
        ("Snacks", "Snacks"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0.01, message="Price must be greater than 0.")],
    )
    description = models.TextField()
    image = models.ImageField(upload_to="food_images/", blank=True, null=True)
    availability = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
