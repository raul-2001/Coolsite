from django.contrib import admin
from players.models import *

class PlayerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Player)
admin.site.register(Category)