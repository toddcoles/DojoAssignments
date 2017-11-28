# declare a class and give it name User
class Bike(object):
    # the __init__ method is called every time a new object is created
    def __init__(self, price, max_speed):
        # set some instance variables. just like any variable we can call these anything
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    # this is a method we created to help a user login
    def displayinfo(self):
        print self.price, self.max_speed, self.miles
        return self

    def ride(self):
        self.miles += 10
        print 'Riding ', self.miles
        return self

    def reverse(self):
        self.miles -= 5
        print 'Reversing', self.miles
        return self
    
#now create an instance of the class
bike_one = Bike(100, "20mph")
bike_one.ride().ride().ride().reverse().displayinfo()
bike_two = Bike(200, "30mph").ride().ride().reverse().reverse().displayinfo()
bike_three = Bike(300, "10mph").reverse().reverse().reverse().displayinfo()