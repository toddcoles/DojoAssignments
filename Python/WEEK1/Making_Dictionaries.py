name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
	if len(arr1) >= len(arr2):
		myKeys=arr1
		myVals=arr2
	else:
		myKeys=arr2
		myVals=arr1

	# print myKeys[0] 
  	new_dict = {}
 	
 	for x in range(len(myKeys)):
 		new_dict.update({myKeys[x]:myVals[x]})
  	return new_dict
  	# print new_dict
print make_dict(name, favorite_animal)