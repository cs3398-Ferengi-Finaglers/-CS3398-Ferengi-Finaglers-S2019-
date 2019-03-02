from django.contrib import admin

# Register your models here.
from .models import Answers, Categories, Questions

admin.site.register(Categories)

#Questions section on the admin interface
class AnswersInline(admin.TabularInline):
    model = Answers
	
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'answertype', 'id')
    inlines = [AnswersInline]
admin.site.register(Questions, QuestionsAdmin)


#Answers section on the admin interface
class AnswersAdmin(admin.ModelAdmin):
    list_display = ('answer', 'belongsTo', 'KNNvalue', 'id')
admin.site.register(Answers, AnswersAdmin)
