import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FoodItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("category", models.CharField(choices=[("Starters", "Starters"), ("Main Course", "Main Course"), ("Desserts", "Desserts"), ("Beverages", "Beverages"), ("Snacks", "Snacks")], max_length=30)),
                ("price", models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0.01, message="Price must be greater than 0.")])),
                ("description", models.TextField()),
                ("image", models.ImageField(blank=True, null=True, upload_to="food_images/")),
                ("availability", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["name"]},
        ),
    ]
