#
# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def dict_conv(x):
	myList = []
	myTuple = ()
	for key, value in x.iteritems():
		myTuple=(key, value)
		myList.append(myTuple)
	print myList
		# print value


dict_conv(my_dict)

#function output
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]