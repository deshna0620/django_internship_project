from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class TelegramUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    first_seen = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username