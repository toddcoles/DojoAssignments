# declare a class and give it name User
class inventory(object):
    # the __init__ method is called every time a new object is created
    def __init__(self, store, owner):
        # set some instance variables. just like any variable we can call these anything
        self.store = store
        self.owner = owner
        self.inv = []


    # this is a method we created to help a user login
    def add_product(self, name):
        self.inv.append(name)
        return self


    def remove_product(self):
        return self
    

    def inventory(self):
        print "Store: ", self.store
        print "Owner: ", self.owner
        for i in range(0, len(self.inv)):
            print "Product ",i+1, self.inv[i]
        return self
        
    
#now create an instance of the class
product_one = inventory("BCGM", "Todd").add_product("pizza").add_product("beer").add_product("fish").inventory()
