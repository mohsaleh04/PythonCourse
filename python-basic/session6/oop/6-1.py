class Human:
	hasBrain: bool
	name: str
	age: int

	def __init__(self, name):
		self.name = name

	def do_raise_hand(self):
		print(f"{self.name} is raising his hand")

	def walk(self):
		print("I am walking")

	def speak(self):
		print("I am speaking")

# class Saleh(Human):
# 	isComputerScientist = True
# 	hasCar = False
#
# 	#constructor
# 	def __init__(self):
# 		self.name = "Saleh2"
# 		self.age = 19
# 		self.hasBrain = True
#
# 	def use_his_laptop(self):
# 		print("I am using my laptop")

# saleh = Saleh()
# print(saleh.name)

#
# saleh = Human()
# saleh.name = "Saleh"
# saleh.age = 19
# saleh.do_raise_hand()
#
# mohammad = Human()
# mohammad.name = "Mohammad"
# mohammad.age = 15
# mohammad.do_raise_hand()
# mohammad.speak()
#
#
