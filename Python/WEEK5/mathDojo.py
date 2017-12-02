class MathDojo(object):
	def __init__(self):

		self.total = 0

	def add(self, *num):
		for x in range(0, len(num)):
			if type(num[x]) is list or type(num[x]) is tuple:
				for y in num[x]:
					self.total += y
			else:
				self.total += num[x]
		return self

	def subtract(self, *num):
		for x in range(0, len(num)):
			if type(num[x]) is list or type(num[x]) is tuple:
				for y in num[x]:
					self.total -= y
			else:
				self.total -= num[x]
		return self

	def result(self):
		print self.total
		return self


a = MathDojo().add(2).add(2,5).subtract(3,2).result()
b = MathDojo().add([1], 3, 4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result()

# print adding