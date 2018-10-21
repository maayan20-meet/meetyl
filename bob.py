import turtle

turtle.addshape("bob.gif")

turtle.shape("bob.gif")

x = 0

turtle.speed(0)



for x in range(360):

	turtle.goto(0,0)
	turtle.right(x)
	turtle.fd(100)
	turtle.right(45)
	turtle.fd(75)
	turtle.right(90)
	turtle.fd(50)

	


turtle.mainloop()