import math
import operator
from django.contrib.auth.models import User
from .models import *

# Will load all users and their attributes into a 2d list that gets passed in
def loadDataset(dataset, currentUser):
	allUsers = User.objects.all()
	allAttributes = Attribute.objects.all()
	
	for i in allUsers:
		print(str(i.id) + " " + str(i))
		
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
			
			if i == currentUser: # Set the current user's data in the set as -1 so they aren't likely to be matched with themselves
				dataset[i.id - 1][attributeIndex] = -1
				
			attributeIndex += 1
	return dataset
	
def euclideanDistance(instance1, instance2, num_of_features):
	distance = 0
	for i in range(num_of_features):
		distance += pow((instance1[i] - instance2[i]), 2)
	return math.sqrt(distance)
	
# Gets passed the data set, the current user's data, and k.
# Given this the function returns the k nearest neighbors.
def getNeighbors(dataset, userInstance, k):
	allAttributes = Attribute.objects.all()
	distances = []
	for i in range(len(dataset)):
		dist = euclideanDistance(userInstance, dataset[i], allAttributes.count())
		distances.append((dataset[i], dist, i)) 
	distances.sort(key=operator.itemgetter(1)) # sorts by distances
	
	neighbors = []
	for i in range(k):
		neighbors.append((distances[i][0], distances[i][2] + 1)) #the neighbors array contains the neighbor's attribute  values and their id
	return neighbors