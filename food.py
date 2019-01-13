import turtle
from turtle import Turtle

class Food(Turtle):
	def __init__(self, x, y, color, r):
		Turtle.__init__(self)
		self.r = r
		self.penup()
		self.realINIT(x, y, color, r)
		self.shape("circle")

	def eat(self, x, y, color, r):
		self.realINIT(x, y, color, r)

	def realINIT(self, x, y, color, r):
		self.goto(x, y)
		self.color(color)
		self.shapesize(r/10)		



