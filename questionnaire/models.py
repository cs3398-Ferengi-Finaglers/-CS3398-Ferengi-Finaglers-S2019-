from django.db import models
from django.contrib.auth.models import User

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
		on_delete=models.SET_NULL,
		blank=True,
		null=True,
		verbose_name="Question Category",
    )
	question = models.TextField(
		max_length=500,
		)
	answertype = models.CharField(
		choices = (
			('SINGLE', 'Can only pick one answer'),
			('MULTIPLE', 'Can pick multiple answers'),
			('SORTABLE', 'The answers are sortable or rateable'),
		),
		default = 'SINGLEANSWER',
		max_length=64,
		verbose_name="Answer Type",
	)
	def getAnswers(self):
		return Answers.objects.filter(belongsTo=self)
	#This function will be used once the forms are properly setup through django
	def getAnswerList(self):
		return [(answer.pk, answer.answer) for answer in
			Answers.objects.filter(belongsTo=self)]
	def __str__(self):
		return self.question
	class Meta:
		verbose_name_plural = "Questions"
		
class Answers(models.Model):
	belongsTo = models.ForeignKey(
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
		
class ResponseInstances(models.Model):
	#ForeignKey pointing to user instance/object will be used once login system is setup
	user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
	    blank=True,
	    null=True,
	    verbose_name="User who answered the question",
    )
	question = models.ForeignKey(
        'Questions',
        on_delete=models.CASCADE,
		verbose_name="Question that was answered",
    )
	answer = models.ForeignKey(
        'Answers',
        on_delete=models.CASCADE,
		blank=False,
		null=False,
		verbose_name="The answer given",
    )
	class Meta:
		verbose_name_plural = "Response Instances"
	