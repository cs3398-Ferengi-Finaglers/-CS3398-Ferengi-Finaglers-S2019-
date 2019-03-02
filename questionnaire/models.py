from django.db import models

# Create your models here.
class Categories(models.Model):
	category = models.CharField(
		verbose_name = 'Category',
		max_length=250, 
		unique=True
		)
	def __str__(self):
		return self.category
	class Meta:
		verbose_name_plural = "Categories"
		
class Questions(models.Model):
	category = models.ForeignKey(
        'Categories',
        on_delete=models.CASCADE,
		verbose_name="Question Category",
    )
	question = models.TextField(
		max_length=500,
		)
	answertype = models.CharField(
		choices = (
			('SINGLE', 'Single Answer'),
			('MULTIPLE', 'Multiple Answers'),
			('SORTABLE', 'Sortable/Rateable Answers'),
		),
		default = 'SINGLEANSWER',
		max_length=64,
		verbose_name="Answer Type",
	)
	def get_answers(self):
		return Answers.objects.filter(belongsToWhichQuestion=self)
	def __str__(self):
		return self.question
	class Meta:
		verbose_name_plural = "Questions"
		
class Answers(models.Model):
	belongsToWhichQuestion = models.ForeignKey(
        'Questions',
        on_delete=models.CASCADE,
		verbose_name="Which question does this answer belong to?"
    )
	answer = models.TextField(max_length=500,)
	KNNvalue = models.FloatField(
		verbose_name="What is the KNN value of this answer?"
	)
	def __str__(self):
		return self.answer
	class Meta:
		verbose_name_plural = "Answers"