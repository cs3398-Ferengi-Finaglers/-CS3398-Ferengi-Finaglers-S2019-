from django.contrib import admin

# Register your models here.
from .models import Answers, Categories, Questions
admin.site.register(Answers)
admin.site.register(Categories)
admin.site.register(Questions)
