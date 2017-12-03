
from datetime import datetime

class Call(object):
    NUM_CALLS = 0
    def __init__(self, name, phone_num, reason):
        self.name = name
        self.phone_num = phone_num
        self.time_of_call = datetime.now()
        self.reason = reason
        self.id = Call.NUM_CALLS
        
        Call.NUM_CALLS += 1
    
    def display_info(self):
        print "\n" + ("#" * 20)
        for attr, val in self.__dict__.iteritems():
            if attr == "time_of_call":
                print "{}: {}".format(attr, val.strftime("%I:%M:%S"))
            else:
                print "{}: {}".format(attr, val)
        print "#" * 20

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = self.get_queue_size()

    def get_queue_size(self):
        return len(self.calls)

    def add(self, a_call):
        self.calls.append(a_call)
        return self
        
# Removal of the calls is not working
    def remove(self, r_call):
    	if r_call in self.calls:
    		self.calls.remove(r_call)
        return self

    def info(self):
        for call in self.calls:
            call.display_info()

call1 = Call("Todd", "(928)848-7182", "Test 1")
call2 = Call("Steve", "(928)848-1234", "Test 2")
call3 = Call("Maria", "(928)848-4321", "Test 3")


cc = CallCenter().add(call1).add(call2).add(call3).info()
dd = CallCenter().remove(call3)
