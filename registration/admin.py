from django.contrib import admin
from .models import Gamer, SelfEvaluation, PreferenceEvaluation

admin.site.register(Gamer)
admin.site.register(SelfEvaluation)
admin.site.register(PreferenceEvaluation)
