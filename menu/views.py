from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import FoodItemForm
from .models import FoodItem


def food_item_list(request):
    food_items = FoodItem.objects.all()
    selected_category = request.GET.get("category", "")

    if selected_category:
        food_items = food_items.filter(category=selected_category)

    categories = FoodItem.CATEGORY_CHOICES

    return render(
        request,
        "menu/food_item_list.html",
        {
            "food_items": food_items,
            "categories": categories,
            "selected_category": selected_category,
        },
    )


def add_food_item(request):
    if request.method == "POST":
        form = FoodItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Food item added successfully.")
            return redirect("food_item_list")
    else:
        form = FoodItemForm()

    return render(
        request,
        "menu/food_item_form.html",
        {"form": form, "page_title": "Add Food Item", "button_text": "Save Food Item"},
    )


def edit_food_item(request, item_id):
    food_item = get_object_or_404(FoodItem, id=item_id)

    if request.method == "POST":
        form = FoodItemForm(request.POST, request.FILES, instance=food_item)
        if form.is_valid():
            form.save()
            messages.success(request, "Food item updated successfully.")
            return redirect("food_item_list")
    else:
        form = FoodItemForm(instance=food_item)

    return render(
        request,
        "menu/food_item_form.html",
        {"form": form, "page_title": "Edit Food Item", "button_text": "Update Food Item"},
    )


def delete_food_item(request, item_id):
    food_item = get_object_or_404(FoodItem, id=item_id)

    if request.method == "POST":
        food_name = food_item.name
        food_item.delete()
        messages.success(request, f'"{food_name}" was deleted from the menu.')
        return redirect("food_item_list")

    return render(request, "menu/food_item_confirm_delete.html", {"food_item": food_item})


def toggle_food_availability(request, item_id):
    if request.method == "POST":
        food_item = get_object_or_404(FoodItem, id=item_id)
        food_item.availability = not food_item.availability
        food_item.save(update_fields=["availability"])

        if food_item.availability:
            messages.success(request, f"{food_item.name} marked as available.")
        else:
            messages.success(request, f"{food_item.name} marked as unavailable.")

    return redirect("food_item_list")
