from django.db import models
from django.contrib.auth.models import User

class GameTable(models.Model):
    name = models.CharField(max_length=100)
    game_select = models.ForeignKey('Games', on_delete=models.CASCADE,)
    description = models.TextField(blank=True)
    leader = models.ForeignKey(User, on_delete=models.CASCADE,)
    creation_date = models.DateField(auto_now_add=True)
    is_full = models.BooleanField()

    def __str__(self):
        return self.name

class Games(models.Model):
    name = models.CharField(max_length=100)
    game_description = models.TextField(blank=True)

    def __str__(self):
        return self.name
