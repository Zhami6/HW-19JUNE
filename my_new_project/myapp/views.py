from django.shortcuts import render
from myapp.models import Item


item = Item.objects.create(title="Первый элемент")
item.save()
items = ["Элемент 1", "Элемент 2", "Элемент 3", "Элемент 4"]

for title in items:
    Item.objects.create(title=title)
items = Item.objects.all()
for item in items:
    item.title = f"{item.title} ({item.id})"
    item.save()
items = Item.objects.all()
for item in items:
    if item.id % 2 != 0:
        item.delete()
