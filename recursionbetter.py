import turtle

n = 1
dis = 100
n = 1
turtle.fd(dis)

def drawRoots(dis, x, y, n):

	turtle.left(45)
	turtle.fd(dis)

	if n == 1:
		n = 2
		drawRoots(dis/2, turtle.xcor(), turtle.ycor(), n)		

	turtle.left(180)
	turtle.fd(dis)

	turtle.left(90)
	turtle.fd(dis)

	if n == 2:
		n = 0
		drawRoots(dis/2, turtle.xcor(), turtle.ycor(), n)

	if n == 0:
		n = 1

	if dis < 1.56:
		dis = -1*dis
		

	return drawRoots(dis, x, y, n)

drawRoots(dis/2, turtle.xcor(), turtle.ycor(), n)