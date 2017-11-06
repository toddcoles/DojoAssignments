#Make a dictionary about myself that contains name, age, country of birth, favorite language
#Make a function that that extracts the data


def about_me(dic):

	# for key, value in dic.items():
		
		print "My name is",
		print dic['name']
		print "My age is",
		print dic['age']
		print "My country of birth is",
		print dic['birth']
		print "My favorite language is",
		print dic['language']


a = {"name":"Todd Coles", "age":45, "birth":"USA", "language":"Python"}
about_me(a)

