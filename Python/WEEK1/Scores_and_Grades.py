import random
random_num = random.random()
# the random function will return a floating point number, that is 0.0 <= random_num < 1.0 or use...
random_num = random.randint(0, 100)
print random_num


# Function to generate random scores
# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

def myGrade(x):
	# grade = ""
	if(x>=90):
		grade="A"
	elif(x>=80):
		grade= "B"
	elif(x>=70):
		grade="C"
	elif(x>=60):
		grade="D"
	else:
		grade="F"
	# print grade
	return grade

def random_grades():
	tot=0
	print "Scores and Grades:"
	for num in range(1,11):
		random_num = random.randint(60, 100)
		tot+=random_num
		print num,
		print "Score: ",
		print random_num,
		print "; Your grade is ",
		print myGrade(random_num)
		
	print "Your average score is a ",
	myAvg = tot/10
	print tot/10,
	print "So your final grade is a " + str(myGrade(myAvg))
	print "End of the program. Bye!"


random_grades()