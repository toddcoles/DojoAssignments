# declare a class and give it name User
class car(object):
    # the __init__ method is called every time a new object is created
    def __init__(self, price, speed, fuel, mileage):
        # set some instance variables. just like any variable we can call these anything
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        global tax
        if price > 10000:
            tax = 0.15
        else:
            tax = 0.12
    # this is a method we created to help a user login
    def displayinfo(self):
        print 'Price ', self.price
        print 'Speed ', self.speed
        print 'Fuel '
        print self.fuel
        print 'Mileage '
        print self.mileage
        print 'Tax ', tax
        return self
    
#now create an instance of the class
car_one = car(2000, "35mph", "Full", "15 mpg").displayinfo()
car_two = car(2000, "5mph", "Not Full", "105 mpg").displayinfo()
car_three = car(2000, "15mph", "Kind of Full", "95 mpg").displayinfo()
car_four = car(2000, "25mph", "Full", "25 mpg").displayinfo()
car_five = car(2000, "45mph", "Empty", "25 mpg").displayinfo()
car_six = car(20000000, "35mph", "Empty", "15 mpg").displayinfo()
