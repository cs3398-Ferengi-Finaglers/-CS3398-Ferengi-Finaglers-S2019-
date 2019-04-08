from django.db import models
from django.contrib.auth.models import User

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