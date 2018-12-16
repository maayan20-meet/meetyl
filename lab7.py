from turtle import *
import turtle
import random
import math
turtle.tracer(0)
turtle.colormode(255)
turtle.hideturtle()

class Ball(Turtle):
	def __init__(self,x, y, radius, color, dx, dy):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.dx = dx
		self.dy = dy
		self.color(color)
		self.pu()

	def move(self, screen_width, screen_height):
		self.goto(self.xcor()+self.dx, self.ycor()+self.dy)
		if(self.xcor() > screen_width or self.xcor() < -screen_width):
			self.dx = -self.dx
		if(self.ycor() > screen_height or self.ycor() < -screen_height):
			self.dy = -self.dy
		

A = Ball(20, 20, 10, 'green', 0.09, 0.015)
B = Ball(15, 40, 12, 'yellow', 0.01, 0.08)
C = Ball(25, 50, 17, 'black', 0.059, 0.08)
D = Ball(32, 32, 20, 'blue', 0.089, 0.045)

Balls = []
Balls.append(A)
Balls.append(B)
Balls.append(C)
Balls.append(D)
def check_collosion():
	for i in Balls:
		for j in Balls:
			if i != j:
				xi = i.xcor()
				yi = i.ycor()

				xj = j.xcor()
				yj = j.ycor()

				DisAB = math.sqrt(math.pow((xi-xj), 2) + math.pow((yi-yj), 2))

				# print(DisAB)
				if(((i.radius + j.radius) >= DisAB)):
					R = random.randint(0, 255)
					G = random.randint(0, 255)
					B = random.randint(0, 255)

					RGB = (R, G, B)
					turtle.bgcolor(RGB)
		
while(True):

	A.move(200, 200)
	B.move(200, 200)
	C.move(200, 200)
	D.move(200, 200)
	check_collosion()
	turtle.getscreen().update()





turtle.mainloop()