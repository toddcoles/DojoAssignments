class animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def run(self):
        self.health -= 5
        return self

    def walk(self):
        self.health -= 1
        return self

    def display_health(self):
        print "Animal name: ", self.name
        print "Health: ", self.health
        
        
class Dog(animal):
    def set_health(self):
    	self.health = 150
    	return self

    def pet(self):
		self.health += 5
		return self

class Dragon(animal):
	def set_health(self):
		self.health = 170
		return self

	def fly(self):
		self.health -= 10
		return self
	
	def display_health(self):
		print "I am a dragon: ", self.name
		print "Health: ", self.health
        

# class Car(Vehicle):
#     def set_wheels(self):
#         self.wheels = 4
#         return self
# class Airplane(Vehicle):
#     def fly(self, miles):
#         self.mileage += miles
#         return self

person = animal("tiger", 50).walk().walk().walk().run().run().display_health()
Nina = Dog("Chihuahua", 150).walk().walk().walk().run().run().pet().display_health()
Mango = Dragon("Green dragon", 10).walk().walk().walk().run().run().fly().display_health()