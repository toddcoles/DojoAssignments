def odd_even(x):
	if(x%2 == 0):
		print "Number is " + str(x) + ". This is an even number."
	else:
		print "Number is " + str(x) + ". This is an odd number."

def multiply(arr, num):
	for item in range(len(arr)):
		# print item*num
		arr[item]*=num
	return arr

for x in range(1, 2001):
	odd_even(x)

a = [2,4,10,16]

print multiply(a, 5)


def layered_multiples(arr):
	new_array=[]
	
  	for nums in arr:
  		myIndex = 1
  		myNum = 0
  		temp_array=[]
  		for myNum in range(1, nums+1):
  			temp_array.append(myIndex)
  		new_array.append(temp_array)
  	return new_array
  	
z = layered_multiples(multiply([2,4,5],3))
print z