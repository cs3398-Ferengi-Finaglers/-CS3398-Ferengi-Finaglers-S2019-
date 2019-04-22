from django.db import models
from django.contrib.auth.models import User
from questionnaire.models import Attribute

# Create your models here.
class Matchmaking(models.Model):
	user = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		blank=True,
		null=True,
		verbose_name="User who requested matchmaking",
	)
	k = models.CharField(max_length=3, 
	choices=(
		('1','1'),
		('2', '2'),
		('3','3'),
		('4','4'),
		('5','5'),
		('6', '6'),
		('7', '7'),
		('8', '8'),
		('9', '9'),
		('10', '10'),
	), default='1')
	neighbors = models.ManyToManyField(User, related_name="neighbors")
  
class MatchmakingAttribute(models.Model):
	user = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		blank=True,
		null=True,
	)
	attribute = models.ForeignKey(
        Attribute,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="What player attribute is being guaged?",
    )
	KNNvalue = models.FloatField(
        verbose_name="What is the KNN value of this user's attribute?"
    )
	
class UserRating(models.Model):
	userDoingTheRating = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		blank=True,
		null=True,
		related_name = "userDoingTheRating",
	)
	userBeingRated = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		blank=True,
		null=True,
		related_name = "userBeingRated",
	)
	aggressionRating = models.IntegerField(
        default = 0,
    )
	skillRating = models.IntegerField(
        default = 0,
    )
	teamworkRating = models.IntegerField(
        default = 0,
    )
	communicationRating = models.IntegerField(
        default = 0,
    )
  
