from turtle import Turtle
import random



class Square(Turtle):
	def __init__(self, size):
		self.shape("square")
		self.size(size)

	def random_color(self):
		self.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

c = Square(10)
c.random_color()