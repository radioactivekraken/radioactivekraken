from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=75)

    def __str__(self):
        return self.name

class GameTable(models.Model):
    name = models.CharField(max_length=100)
    #champaign = models.CharField(max_length=100)
    game_select = models.ForeignKey('Games', on_delete=models.CASCADE,)
    description = models.TextField(blank=True)
    #leader = models.ForeignKey('Person', on_delete=models.CASCADE, blank=True)
    creation_date = models.DateTimeField()
    #players = models.ForeignKey('Players_Table', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Players_Table(models.Model):
    name = models.ManyToManyField('GameTable')
    leader_name = models.ForeignKey('Person', on_delete=models.CASCADE,)
    player_name = models.ManyToManyField('Person')

class Games(models.Model):
    name = models.CharField(max_length=100)
    game_description = models.TextField(blank=True)

    def __str__(self):
        return self.name
