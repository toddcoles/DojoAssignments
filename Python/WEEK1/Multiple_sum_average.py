#Print all odd numbers from 1 to 1,000
for x in range(1, 1000, 2):
	print x

#Print multiples of 5 from 5 to 1,000,000
print(list(range(5, 1000000, 5)))

#Print the sum of a list
a = [1, 2, 5, 10, 255, 3]
print sum(a)

#Print the average of the list
a = [1, 2, 5, 10, 255, 3]
print sum(a)/len(a)