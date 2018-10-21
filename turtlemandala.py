import turtle
x = 1
y = 0 
turtle.speed(0)
turtle.hideturtle()
turtle.color("Purple")

while True:
	turtle.forward(x)
	turtle.left(100)
	x = x + 0.1
	y = y + 1 

	if y == 100:
		turtle.color("Red")

	if y == 200:
		turtle.color("Yellow")

	if y == 300:
		turtle.color("Purple")
		y = 0
turtle.mainloop()
