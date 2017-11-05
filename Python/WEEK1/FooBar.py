#You must import math for the math fuctions to work in Python
import math

#this function checks for square root
def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        return True
    else:
        return False

#This function checks for prime number
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False

#Testing for a square root and prime number
for x in range(100,100000):
	if(is_square(x) == True):
		print str(x) + "Bar"
	elif(is_prime(x) == False):
		print str(x) + "Foo"
	else:
		print str(x) + "Foo Bar"



