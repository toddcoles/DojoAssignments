#This prints the lines depending on the modulo 
for x in range(0,13):
	if x == 0:
		print "x",
		continue
	else:
		print "\t" + str(x),
print "\n"

for i in range(1,13):
	print i,
	for y in range(1,13):
		if(len(str(y*i))>2):
			print y*i,
		else:
			print "\t" + str(y*i),
	print "\n"
		

