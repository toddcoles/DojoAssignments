# declare a class and give it name User
class product(object):
    # the __init__ method is called every time a new object is created
    def __init__(self, name, brand, price, weight, status):
        # set some instance variables. just like any variable we can call these anything
        self.name = name
        self.brand = brand
        self.price = price
        self.weight = weight
        self.status = "for sale"
        # self.status = "for sale"
        # self.tax = tax
        # global status
        # if  > 10000:
        #     tax = 0.15
        # else:
        #     tax = 0.12
    # this is a method we created to help a user login
    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax):
        self.tax = tax
        self.price = self.price + (self.price * self.tax)
        print self.price
        return self

    def prod_return(self, reason):
        self.reason = reason
        if self.reason == "defective":
            self.status = "defective"
            self.price = 0
        elif self.reason == "like new":
            self.status = "for sale"
            self.price = self.price * .8
        return self

    def displayinfo(self):
        print "Product: ", self.name
        print "Brand: ", self.brand
        print "Price: ", self.price
        print "Weight: ", self.weight
        print "Status: ", self.status
        return self
        
    
#now create an instance of the class
product_one = product("T-shirt", "Nike", 20, "8 oz", "for sale").displayinfo().add_tax(0.05).prod_return("defective").displayinfo()
product_two = product("Pants", "Levi", 25, "1 lb", "for sale").displayinfo().add_tax(0.03).prod_return("like new").displayinfo()
product_three = product("laptop", "Dell", 1300, "6 lbs", "for sale").displayinfo().sell().displayinfo()
product_four = product("Ipad", "Apple", 800, "3 lbs", "for sale").displayinfo().add_tax(0.05).sell().displayinfo()
product_five = product("Printer", "HP", 450, "25 lbs", "for sale").displayinfo().add_tax(0.03).prod_return("defective").displayinfo()
