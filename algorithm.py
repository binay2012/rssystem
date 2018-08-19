import time
from models import *
from math import sqrt


def similarity_score(person1,person2):
	dataset = get_dataset()
	
	# Returns ratio Euclidean distance score of person1 and person2 
	viewed = {}		# To get both rated items by person1 and person2

	for item in dataset[person1]:
		if item in dataset[person2]:
			viewed[item] = 1

		# Conditions to check they both have an common rating items	
		if len(viewed) == 0:
			return 0

		# Finding Euclidean distance 
		sum_of_eclidean_distance = []	

		for item in dataset[person1]:
			if item in dataset[person2]:
				sum_of_eclidean_distance.append(pow(dataset[person1][item] - dataset[person2][item],2))
		sum_of_eclidean_distance = sum(sum_of_eclidean_distance)

		return 1/(1+sqrt(sum_of_eclidean_distance))



def person_correlation(person1,person2):
	dataset = get_dataset()
	# To get both rated items
	
	ratedbyboth = {}
	isbn_list = []
	similar = []

	for id, isbn in dataset.iteritems():
		if id  == person1:
			for i in isbn:
				print i
				isbn_list.append(i)
	for id2, isbn2 in dataset.iteritems():
		if id2 == person2:
			for i2 in isbn2:
				for x in isbn_list:
					if i2 == x:
						ratedbyboth[i2] = 1

	

	# person1 =str(person1)
	# person2 = str(person2)
	# print dataset[person1]
	# for item in dataset[person1]:
	# 	if item in dataset[person2]:
	# 		ratedbyboth[item] = 1

	ratings = len(ratedbyboth)
	print ratings
	# Checking for number of ratings in common
	if ratings == 0:
		return 0

	# Add up all the preferences of each user
	person1_preferences_sum = sum([dataset[person1][item] for item in ratedbyboth])
	person2_preferences_sum = sum([dataset[person2][item] for item in ratedbyboth])

	# Sum up the squares of preferences of each user
	person1_square_preferences_sum = sum([pow(dataset[person1][item],2) for item in ratedbyboth])
	person2_square_preferences_sum = sum([pow(dataset[person2][item],2) for item in ratedbyboth])

	# Sum up the product value of both preferences for each item
	product_sum_of_both_users = sum([dataset[person1][item] * dataset[person2][item] for item in ratedbyboth])

	# Calculate the person score
	numerator_value = product_sum_of_both_users - (person1_preferences_sum*person2_preferences_sum/ratings)
	denominator_value = sqrt((person1_square_preferences_sum - pow(person1_preferences_sum,2)/ratings) * (person2_square_preferences_sum -pow(person2_preferences_sum,2)/ratings))
	if denominator_value == 0:
		return 0
	else:
		rate = numerator_value/denominator_value
		return rate 

def most_similar_users(person,number_of_users):
	dataset = get_dataset()
	# returns the number_of_users (similar persons) for a given specific person.
	scores = [(person_correlation(person,other_person),other_person) for other_person in dataset if  other_person != person ]
	
	# Sort the similar persons so that highest scores person will appear at the first
	scores.sort()
	scores.reverse()
	return scores[0:number_of_users]

def user_recommendations(person):
	person=str(person)

	dataset = get_dataset() #GETS data set
	# Gets recommendations for a person by using a weighted average of every other user's rankings
	print dataset
	totals = {}
	simSums = {}
	rankings_list =[]
	for other in dataset:
		other = str(other)
		# don't compare me to myself
		if other == person:
			continue

		sim = person_correlation(person,other)
		print sim


		# ignore scores of zero or lower
		if sim <=0: 
			continue
		for item in dataset[other]:

			# only score movies i haven't seen yet
			if item not in dataset[person] or dataset[person][item] == 0:

			# Similrity * score
				totals.setdefault(item,0)
				totals[item] += dataset[other][item]* sim
				# sum of similarities
				simSums.setdefault(item,0)
				simSums[item]+= sim

		# Create the normalized list

	rankings = [(total/simSums[item],item) for item,total in totals.items()]
	rankings.sort()
	rankings.reverse()
	# returns the recommended items
	recommendataions_list = [recommend_item for score,recommend_item in rankings]
	return recommendataions_list




