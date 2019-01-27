import turtle
from turtle import Screen
import time
import random
import math
import os
from ball import Ball
from food import Food

turtle.tracer(0)
turtle.hideturtle()

turtle.bgpic("white.gif")

RUNNING = True
SLEEP = 0.008
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 30
MINIMUM_BALL_DX = -6
MAXIMUM_BALL_DX = 6
MINIMUM_BALL_DY = -6
MAXIMUM_BALL_DY = 6

FOOD_VALUE = 3
FOOD_SIZE = 4

UNDER_SCORE = 20

NUMBER_OF_FOOD = 30

FUTURE_SEEING = 5
PREY_RADIUS = 40

LEADERS = 3
my_color = (random.random(), random.random(), random.random())

MY_BALL = Ball(0, 0, 0, 0, random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS - 5), my_color)
MY_SCORE = turtle.Turtle()

MY_SCORE.penup()
MY_SCORE.hideturtle()

BALLS = []
FOOD = []
SCORE = []

turtle.register_shape("gold.gif")
turtle.register_shape("silver.gif")
turtle.register_shape("bronze.gif")
'''
functin will set all the need parameters for staarting the game
input: none
ouput: none
'''
def start_game():

	f = open("leaderbord.txt", 'a')

	f.write('a')
	f = open("leaderbord.txt", 'r')

	if f.read(1) == 'a':
		f = open("leaderbord.txt", 'w')
		for i in range(LEADERS):
			f.write("0\n")
	f.close()


	bord = turtle.Turtle()
	bord.penup()
	bord.shapesize(5)

	f = open("leaderbord.txt", 'r')
	fflist = f.readlines()
	bord.shape("gold.gif")
	bord.goto(-SCREEN_WIDTH + 50, SCREEN_HEIGHT - 50)
	bord.write(fflist[0], font=("Ariel", 15, "bold"))
	bord.goto(-SCREEN_WIDTH + 20, SCREEN_HEIGHT - 25)
	bord.stamp()
	bord.shape("silver.gif")
	bord.goto(-SCREEN_WIDTH + 50, SCREEN_HEIGHT - 100)
	bord.write(fflist[1], font=("Ariel", 15, "bold"))
	bord.goto(-SCREEN_WIDTH + 20, SCREEN_HEIGHT - 75)
	bord.stamp()
	bord.shape("bronze.gif")
	bord.goto(-SCREEN_WIDTH + 50, SCREEN_HEIGHT - 150)
	bord.write(fflist[2], font=("Ariel", 15, "bold"))
	bord.goto(-SCREEN_WIDTH + 20, SCREEN_HEIGHT - 125)
	bord.stamp()


	#create all balls objects
	for i in range(NUMBER_OF_BALLS):
		ballx = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
		bally = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)

		dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
		dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)

		radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)

		color = (random.random(), random.random(), random.random())

		newBall = Ball(ballx, bally, dx, dy, radius, color)

		BALL = []

		BALLS.append(newBall)

	#create all food object
	for i in range(NUMBER_OF_FOOD):
		foodx = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
		foody = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)

		color = (random.random(), random.random(), random.random())

		newFood = Food(foodx, foody, color, FOOD_SIZE)

		FOOD.append(newFood)

	#create all score turtles
	for i in range(NUMBER_OF_BALLS):
		i = turtle.Turtle()
		i.hideturtle()
		i.penup()

		SCORE.append(i)

'''
function will move a ball, using the ball.move() function
input: none
output: none
'''
def move_ball(ball):
	ball.move(SCREEN_WIDTH, SCREEN_HEIGHT)

'''
function will move all scores
input: none
output: none
'''
def move_all_score():
	for score in SCORE:
		score.goto(BALLS[SCORE.index(score)].xcor(), BALLS[SCORE.index(score)].ycor() - BALLS[SCORE.index(score)].r - 20)
		score.clear()
		score.write(str(BALLS[SCORE.index(score)].r),align=("center"), font=("Ariel", 15, "normal"))

'''
function will move my scores
input: none
output: none
'''
def move_my_score():
	MY_SCORE.goto(MY_BALL.xcor(), MY_BALL.ycor() - MY_BALL.r - UNDER_SCORE)
	MY_SCORE.clear()
	MY_SCORE.write(str(MY_BALL.r),align=("center"), font=("Ariel", 15, "normal"))

'''
function will check if two balls are colliding
input: two balls
output: true / false (acording to if there was a collision or not)
'''
def collide(ball_a, ball_b):
	if(ball_a == ball_b):
		return False

	xa = ball_a.xcor()
	ya = ball_a.ycor()

	xb = ball_b.xcor()
	yb = ball_b.ycor()

	disab = math.sqrt(math.pow((xa-xb), 2) + math.pow((ya-yb), 2))
	if(ball_a.r + ball_b.r >= disab):
		return True
	return False

'''
function will use the collide function and create new ball in the case of collision
input: none
output: none
'''
def check_collision(ball_a, ball_b):
	if(collide(ball_a, ball_b)):
		ball_a_r = ball_a.r
		ball_b_r = ball_b.r

		if(ball_a_r < ball_b_r):
			kill(ball_a)
			ball_b.r += int(ball_val(ball_a))
			ball_b.shapesize(ball_b.r/10)

		elif(ball_a_r > ball_b_r):
			kill(ball_b)
			ball_a.r += int(ball_val(ball_b))
			ball_a.shapesize(ball_a.r/10)

'''
function will check if there is a ball object that is colliding with a food object and change the parameters of each
input: none
output: none
'''
def  check_food_collision(ball):
	for food in FOOD:
		if(collide(ball, food)):
			new_x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
			new_y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			new_color = (random.random(), random.random(), random.random())

			food.eat(new_x, new_y, new_color, FOOD_SIZE)
			ball.r += FOOD_VALUE
			ball.shapesize(ball.r/10)

'''
function will check if there is a collision with my ball
input: none
output: true / false (if there is collision and ball.r is bigger, then function returns false to stop the game)
'''
def check_myball_collision():
	for ball in BALLS:
		if(collide(ball, MY_BALL)):
			ball_r = ball.r
			my_ball_r = MY_BALL.r
			if(ball_r > my_ball_r):
				return False

			kill(ball)
			MY_BALL.r += int(ball_val(ball))
			MY_BALL.shapesize(MY_BALL.r/10)
	return True

'''
function checks if MY_BALL is colliding with food object
input: none
output: none
'''
def check_myball_food():
	for food in FOOD:
		if(collide(MY_BALL, food)):
			new_x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
			new_y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			new_color = (random.random(), random.random(), random.random())

			food.eat(new_x, new_y, new_color, FOOD_SIZE)
			MY_BALL.r += int(FOOD_VALUE/2)
			MY_BALL.shapesize(MY_BALL.r/10)

	return True

'''
function will move MY_BALL with binding to mouse
input: none
output: none
'''
def movearound(event):
	x = event.x - SCREEN_WIDTH
	y = SCREEN_HEIGHT - event.y

	MY_BALL.goto(x, y)

'''
function will change ball direction if in the future it is colliding with a bigger ball
input: ball to be checked
ouput: false (only to stop the function to save memory)
'''
def prey(cur_ball):
	for dif_ball in BALLS:
		if(dif_ball.r > cur_ball.r):
			if(check_near(cur_ball, dif_ball) < dif_ball.r + PREY_RADIUS*FUTURE_SEEING
				):
				if check_future(cur_ball, dif_ball):
					cur_ball.changeDir(random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX), random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY))
					return False

'''
checks if two balls are near each other
input: two balls
ouput: distance between the balls
'''
def check_near(ball_a, ball_b):

	disab = math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(), 2) + math.pow(ball_a.ycor()-ball_b.ycor(), 2))
	return disab

'''
function will calculate the upcoming positions of two balls and determine if they are colliding in the future or not
input: two balls
ouput: true / false (according to whatever balls are to be colliding)
'''
def check_future(prey, predetor):
	for i in range(FUTURE_SEEING):
		prey_dx = prey.xcor() + prey.dx*(i + 1)
		prey_dy = prey.ycor() + prey.dy*(i + 1)
		predetor_dx = predetor.xcor() + predetor.dx*(i + 1)
		predetor_dy = predetor.ycor() + predetor.dy*(i + 1)

		D = math.sqrt(pow(predetor_dx - prey_dx, 2) + pow(predetor_dy - prey_dy, 2))

		if(prey.r + predetor.r >= D):
			return True
	return False

'''
functin will set new parameters to a ball
input: ball to be killed
output: none
'''
def kill(ball):
	new_x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	new_y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	new_dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	new_dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	while(new_dx == 0 and new_dy == 0):
		new_dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
		new_dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	new_radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	new_color = (random.random(), random.random(), random.random())
	ball.kill(new_x, new_y, new_dx, new_dy, new_radius, new_color)

'''
function will return the value of a ball
input: ball to check value
output: the balls value
'''
def ball_val(ball):
	return int(ball.r/2)
		
turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

start_game()

while RUNNING:
	if(SCREEN_WIDTH == turtle.getcanvas().winfo_width()/2 or SCREEN_HEIGHT == turtle.getcanvas().winfo_height()/2):
		SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
		SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

		for ball_a in BALLS:
			if (ball_a.r < PREY_RADIUS):
				prey(ball_a)
			move_ball(ball_a)
			check_food_collision(ball_a)
			for ball_b in BALLS:
				check_collision(ball_a, ball_b)
		
		check_myball_food()
		move_all_score()
		move_my_score()
		RUNNING = check_myball_collision()
		turtle.update()
		time.sleep(SLEEP)

text = turtle.Turtle()
text.penup()
text.goto(-75, 0)
text.write("GAME OVER!", font=("Ariel", 20, "bold"))

f = open("leaderbord.txt", 'r')

flist = f.readlines()
leaders = ['a', 'a', 'a']
first = int(flist[0])
second = int(flist[1])
third = int(flist[2])

f = open("leaderbord.txt", 'w')

if(MY_BALL.r > int(first)):
	f.write(str(MY_BALL.r) + '\n')
	f.write(str(first) + '\n')
	f.write(str(second) + '\n')
elif(MY_BALL.r > int(second)):
	f.write(str(first) + '\n')
	f.write(str(MY_BALL.r) + '\n')
	f.write(str(second) + '\n')
elif(MY_BALL.r > third):
	f.write(str(first) + '\n')
	f.write(str(second) + '\n')
	f.write(str(MY_BALL.r) + '\n')
elif(MY_BALL.r <= third):
	f.write(str(first) + '\n')
	f.write(str(second) + '\n')
	f.write(str(third) + '\n')

turtle.mainloop()