#First, the function took a list of integers and converted them to stars
#Second, the function now takes integers and/or strings and converts the strings to the first letter of the string in lower case


def draw_stars(arr):
	for items in range(len(arr)):
		# print arr[items]
		# print items
		if(type(arr[items]) == str):
			for letters in range(len(arr[items])):
				print arr[items][0:1].lower(),
		elif(type(arr[items]) == int):
			for stars in range(arr[items]):
				print "*",
		print "\n"


a = [4, 6, 1, 3, 5, 7, 25]
draw_stars(a)


x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)