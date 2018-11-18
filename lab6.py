import turtle
from turtle import Turtle
import random
#import screen 


class Rectangle(Turtle):
	def __init__(self, width, height):

		Turtle.__init__(self)

		turtle.home()
		turtle.penup()
		turtle.hideturtle()
		turtle.begin_poly()
		turtle.fd(height)
		turtle.left(90)
		turtle.fd(width)
		turtle.left(90)
		turtle.fd(height)
		turtle.left(90)
		turtle.fd(width)
		turtle.end_poly()
		q = turtle.get_poly()
		turtle.register_shape("custom_rect", q)

		self.shape("custom_rect")

#a = Rectangle(100, 200)

#turtle.mainloop()




turtle.colormode(255)



class Square(Turtle):
	def __init__(self, size, speed):
		Rectangle.__init__(self, size, size)

		self.size = size

		self.speed = speed


	def random_color(self):
		
		R = random.randint(0, 255)
		G = random.randint(0, 255)
		B = random.randint(0, 255)

		RGB = (R, G, B)
		print(RGB)

		self.color(RGB)

	def speed(self):
		self.speed(self.speed)

	def say_size(self):
		print("My size is " + str(self.size) + "!")

	def move(self):

		while (True):

			self.fd(1)

			postx = turtle.xcor()
			posty = turtle.ycor()

			if (postx > 50 or postx < -50 or posty > 50 or posty < -50):
				turtle.left(90)
				turtle.left(random.randint())


bob = Square(10, 20)
bob.random_color()
bob.say_size()

bob.move()


turtle.mainloop()




'''
class Hexagon(Turtle):
	def __init__(self, size):
		Turtle.__init__(self)

		turtle.home()
		turtle.penup()
		turtle.hideturtle()
		turtle.begin_poly()
		turtle.fd(size)
		turtle.left(60)
		turtle.fd(size)
		turtle.left(60)
		turtle.fd(size)
		turtle.left(60)
		turtle.fd(size)
		turtle.left(60)
		turtle.fd(size)
		turtle.left(60)
		turtle.fd(size)
		turtle.end_poly()
		p = turtle.get_poly()
		turtle.register_shape("Hexagon", p)

		self.penup()

		self.shape("Hexagon")



	def jump(self):
		self.left(90)
		self.fd(100)


a = Hexagon(20)
a.jump()
		

turtle.mainloop()

'''



