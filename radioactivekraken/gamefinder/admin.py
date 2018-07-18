from django.contrib import admin

from .models import GameTable
from .models import Games

@admin.register(GameTable)
class GameTableAdmin(admin.ModelAdmin):
    list_display = ['name', 'game_select', 'description', 'leader', 'creation_date', 'is_full']

@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ['name', 'game_description']
