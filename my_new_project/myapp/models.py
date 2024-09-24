from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
