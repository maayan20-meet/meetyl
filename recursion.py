import turtle


turtle.hideturtle()
turtle.fd(100)

def branch(dis, n):
	n += 1

	turtle.left(45)
	turtle.fd(dis)
	
	if n == 1:
		branch(dis/2, n)

	turtle.left(180)
	turtle.fd(dis)

	turtle.left(90)
	turtle.fd(dis)

	turtle.left(180)
	turtle.fd(dis)
branch(50, 0)
	
turtle.mainloop()