from django.shortcuts import render
from myapp.models import Item
from .models import Task


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

from django.shortcuts import render
from .models import Task


def TaskListView(request):
    tasks = Task.objects.values("title", "completed")
    return render(request, "tasks/task_list.html", {"tasks": tasks})


def TaskCreateView(request):
    pass


def TaskDetailView(request, id):
    pass


def TaskUpdateView(request, id):
    pass


def TaskDeleteView(request, id):
    pass
