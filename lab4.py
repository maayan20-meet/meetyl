'''
class Animal(object):
	def __init__(self, sound, name, age, favorite_food):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_food = favorite_food
	def eat(self):
		print("Yummy! " + self.name + " is eating " + self.favorite_food)
	def make_sound(self, x):
		print(self.sound*x)

dog = Animal("Bark", "Marly", "5", "carrot")
dog.eat()
dog.make_sound(5)
'''

'''
class Person(object):
	def __init__(self, name, age, gender, fav_breakfast, origin):
		self.name = name
		self.age = age
		self.gender = gender
		self.fav_breakfast = fav_breakfast
		self.origin = origin
	def eat_breakfast(self):
		print(self.name + " is eating " + self.fav_breakfast + "!")
	def where(self):
		print(self.name + " came from " + self.origin + "!")

j = Person("Hope", 23, "female", "granola", "USA")
j.eat_breakfast()
j.where()
'''

class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
	def sing(self):
		for x in range(len(self.lyrics)):
			print(self.lyrics[x])

flower_song = Song(["Roses are red,", "Violets are blue,", "I wrote this poem for you."])
dont_worry = Song(["dont worry", "be happy", "dont worry be happy"])
dont_worry.sing()
flower_song.sing()