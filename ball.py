import turtle
import random
from turtle import Turtle



class Ball(Turtle):
	def __init__(self, x, y, dx, dy, r, color):
		Turtle.__init__(self)
		self.penup()
		self.shape("circle")
		self.realINIT(x, y, dx, dy, r, color)

	def move(self, screen_width, screen_height):
		current_x = self.xcor()
		new_x = current_x + self.dx

		current_y = self.ycor()
		new_y = current_y + self.dy

		sides = {'right':new_x + self.r, 'left':new_x - self.r, 'up':new_y + self.r, 'down':new_y - self.r}

		self.bottom = sides['down'] #for the score text

		self.goto(new_x, new_y)

		if(sides['right'] > screen_width or sides['left'] < (-screen_width)):
			self.dx *= -1
			if(new_x > 0):
				self.setx(screen_width - self.dx - self.r - 0.001)
			if(new_x < 0):
				self.setx((-screen_width) + self.dx + self.r + 0.001) 

		if(sides['up'] > screen_height or sides['down'] < (-screen_height)):
			self.dy *= -1
			if(new_y > 0):
				self.sety(screen_height - self.dy - self.r  - 0.001)
			if(new_y < 0):
				self.sety((-screen_height) + self.dy + self.r  + 0.001)



	def kill(self, x, y, dx, dy, r, color):
		self.realINIT(x, y, dx, dy, r, color)

	def realINIT(self, x, y, dx, dy, r, color):
		self.goto(x, y)
		self.dx = dx
		self.dy = dy
		self.r = r

		self.shapesize(r/10)
		self.color(color)

	def changeDir(self, dx, dy):
		self.dx = dx
		self.dy = dy


'''
a = Ball(0, 0, 5, 5, 20, 'purple')

while True:
	a.move(100, 100)
'''