from django.contrib import admin
from .models import *

# Register your models here.
class MatchmakingAdmin(admin.ModelAdmin):
    list_display = ('user', 'k')
admin.site.register(Matchmaking, MatchmakingAdmin)

class MatchmakingAttributeAdmin(admin.ModelAdmin):
    list_display = ('user', 'attribute', 'KNNvalue')
admin.site.register(MatchmakingAttribute, MatchmakingAttributeAdmin)

admin.site.register(UserRating)
