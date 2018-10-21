import turtle
import random

colors = ["red","blue","green","purple"]

for x in range(390):
	x = random.randint(-100,100)
	y = random.randint(-100,100)
	color = random.choice(colors)
	turtle.color(color)
	turtle.goto(x,y)