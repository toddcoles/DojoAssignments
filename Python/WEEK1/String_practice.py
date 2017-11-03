#Find the first instance of "day"
words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")

#Find the min and max of the list x
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

#Find the first and last elements of the list x
x = ["hello",2,54,-2,7,12,98,"world"]
print "First element is: "
print x[0:1]
print "Last element is: "
print x[-1::]

#Sort the list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
temp = sorted(x)
print temp
#Get the first half of the list and put in temporary variable
temp_list = temp[0:len(temp)/2]
print temp_list
#Get second half of list into new list variable
new_list = temp[5:]
print new_list
#Insert new list into position 0 of new list variable
new_list[0] = temp_list
print new_list