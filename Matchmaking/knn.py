import math

def euclideanDistance(instance1, instance2, num_of_features):
	distance = 0
	for i in range(num_of_features):
		distance += pow((instance1[i] - instance2[i]), 2)
	return math.sqrt(distance)