from django import forms
from .models import FoodItem


class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = [
            "name",
            "category",
            "price",
            "description",
            "image",
            "availability",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter food name"}),
            "price": forms.NumberInput(attrs={"step": "0.01", "min": "0.01", "placeholder": "e.g. 180"}),
            "description": forms.Textarea(attrs={"rows": 4, "placeholder": "Describe the food item"}),
        }

    def clean_name(self):
        name = self.cleaned_data.get("name", "").strip()
        if not name:
            raise forms.ValidationError("Food name cannot be empty.")
        return name

    def clean_category(self):
        category = self.cleaned_data.get("category", "").strip()
        if not category:
            raise forms.ValidationError("Please select a category.")
        return category

    def clean_description(self):
        description = self.cleaned_data.get("description", "").strip()
        if not description:
            raise forms.ValidationError("Description cannot be empty.")
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is not None and price <= 0:
            raise forms.ValidationError("Price must be greater than 0.")
        return price
