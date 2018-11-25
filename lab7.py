from turtle import *
import turtle
import random
import math


class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
		self.pu()

A = Ball(20, 'red', 1)
B = Ball(15, 'yellow', 2)
C = Ball(25, 'green', 1)
D = Ball(32, 'orange', 2)

def check_collosion(Ball1, Ball2, Ball3, Ball4):
	
	Balls = []

	Balls.append(Ball1)
	Balls.append(Ball2)
	Balls.append(Ball3)
	Balls.append(Ball4)

	
	for i in Balls:

		for j in Balls:

			xi = i.xcor()
			yi = i.ycor()

			xj = j.xcor()
			yj = j.ycor()


			DisAB = math.sqrt(math.pow((xi-xi), 2) + math.pow((yi-yj), 2))

			if ((i != j) and (i.radius + j.radius > DisAB)):
				if (i.radius < j.radius):
					i.goto(random.randint(-200, 200), random.randint(-200, 200))
				elif (j.radius < i.radius):
					j.goto(random.randint(-200, 200), random.randint(-200, 200))



def move(Ball):

	
	if(Ball.xcor() < -200 or Ball.xcor() > 200 or Ball.ycor() < -200 or Ball.ycor() > 200):
		Ball.left(90 + random.randint(1, 179))
	else:
		Ball.fd(1)
		check_collosion(A, B, C, D)

while(True):

	move(A)






turtle.mainloop()