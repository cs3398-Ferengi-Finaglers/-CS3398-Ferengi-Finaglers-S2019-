from django.contrib import admin

# Register your models here.
from .models import Matchmaking

class MatchmakingAdmin(admin.ModelAdmin):
    list_display = ('user', 'k')
admin.site.register(Matchmaking, MatchmakingAdmin)
