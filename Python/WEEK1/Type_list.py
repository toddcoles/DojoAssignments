#input
l = ['magical unicorns',19,'hello',98.98,'world']
# input
# l = [2,3,1,7,4,12]
# input
# l = ['magical','unicorns']

theSum = 0
theString = ''

for item in l:
	print type(item)
		
	if(type(item) == int or type(item) == float):
		theSum+=item
	elif(type(item) == str):
		theString+= item + " "

if(all(isinstance(x, (int, float)) for x in l)):
	print "The list you entered is of number type"
	print "Sum: " + str(theSum)
elif(all(isinstance(x, (str)) for x in l)):
	print "The list you entered is of string type"
	print theString
else:
	print "The list you entered is of mixed type"
	print "Sum: " + str(theSum)
	print theString



