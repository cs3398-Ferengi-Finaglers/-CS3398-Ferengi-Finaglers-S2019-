from django.db import models

# Create your models here.
class Questions(models.Model):
	type = models.CharField(
		choices = (
			('GENERAL', 'general'),
			('SANDBOX', 'sandbox'),
			('SHOOTER', 'shooter'),
			('STRATEGY', 'strategy'),
		),
		default = 'GENERAL',
		max_length=64,
	)
	question = models.TextField(max_length=500,)
	#answers = models.TextField(max_length=1000,)
	def __str__(self):
		return self.question
	class Meta:
		verbose_name_plural = "Questions"
		
class Answers(models.Model):
	belongsToWhichQuestion = models.ForeignKey(
        'Questions',
        on_delete=models.CASCADE,
    )
	answer = models.TextField(max_length=500,)
	KNNvalue = models.FloatField()
	def __str__(self):
		return self.answer
	class Meta:
		verbose_name_plural = "Answers"