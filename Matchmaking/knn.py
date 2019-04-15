import math
from django.contrib.auth.models import User
from .models import *

# Will load all users and their attributes into a 2d list that gets passed in
def loadDataset(dataset):
	allUsers = User.objects.all()
	allAttributes = Attribute.objects.all()
	
	for i in allUsers:
		attributeIndex = 0
		for attribute in allAttributes:
			try:
				userAttributeInstance = MatchmakingAttribute.objects.get(user=i, attribute=attribute)
			except MatchmakingAttribute.DoesNotExist:
				print('user ' + str(i) + ' does not have a value assigned for one of their attributes: '
				+ str(attribute))
				dataset[i.id - 1][attributeIndex] = 0
				break
				
			dataset[i.id - 1][attributeIndex] = userAttributeInstance.KNNvalue
			attributeIndex += 1
	return dataset
	
def euclideanDistance(instance1, instance2, num_of_features):
	distance = 0
	for i in range(num_of_features):
		distance += pow((instance1[i] - instance2[i]), 2)
	return math.sqrt(distance)