import turtle
from turtle import Screen
import time
import random
import math
from ball import Ball
from food import Food

turtle.tracer(0,0)
turtle.hideturtle()

RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 50
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

NUMBER_OF_FOOD = 20

my_color = (random.random(), random.random(), random.random())

MY_BALL = Ball(0, 0, 0, 0, random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS - 20), my_color, 0)

BALLS = []
FOOD = []
FBALLS = []

for i in range(NUMBER_OF_BALLS):
	ballx = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	bally = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)

	dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)

	radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)

	color = (random.random(), random.random(), random.random())

	newBall = Ball(ballx, bally, dx, dy, radius, color, 0)

	BALLS.append(newBall)

for i in range(NUMBER_OF_FOOD):
	foodx = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	foody = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)

	color = (random.random(), random.random(), random.random())

	newFood = Food(foodx, foody, color, 4)

	FOOD.append(newFood)


def move_all_balls():
	for i in BALLS:
		i.move(SCREEN_WIDTH, SCREEN_HEIGHT)

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

def check_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if(collide(ball_a, ball_b)):
				ball_a_r = ball_a.r
				ball_b_r = ball_b.r

				new_x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				new_y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				new_dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				new_dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				while(new_dx == 0 and new_dy == 0):
					new_dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
					new_dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				new_radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				new_color = (random.random(), random.random(), random.random())

				if(ball_a_r < ball_b_r):
					ball_a.kill(new_x, new_y, new_dx, new_dy, new_radius, new_color, 0)
					ball_a.shapesize(new_radius/10)
					ball_b.r += 1
					ball_b.shapesize(ball_b.r/10)

				elif(ball_a_r > ball_b_r):
					ball_b.kill(new_x, new_y, new_dx, new_dy, new_radius, new_color, 0)
					ball_a.r += 1
					ball_a.shapesize(ball_b.r/10)

def  check_food_collision():
	for ball in BALLS:
		for food in FOOD:
			if(collide(ball, food)):
				new_x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				new_y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				new_color = (random.random(), random.random(), random.random())

				food.eat(new_x, new_y, new_color, 4)
				ball.r += 1
				ball.shapesize(ball.r/10)

def check_myball_collision():
	for ball in BALLS:
		if(collide(ball, MY_BALL)):
			ball_r = ball.r
			my_ball_r = MY_BALL.r
			if(ball_r > my_ball_r):
				return False

			new_x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
			new_y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			new_dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
			new_dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
			while(new_dx == 0 and new_dy == 0):
				new_dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				new_dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
			new_radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
			new_color = (random.random(), random.random(), random.random())

			ball.kill(new_x, new_y, new_dx, new_dy, new_radius, new_color, 0)
			ball.shapesize(new_radius/10)
			MY_BALL.r += 1
			MY_BALL.shapesize(MY_BALL.r/10)
	return True

def check_myball_food():
	for food in FOOD:
		if(collide(MY_BALL, food)):
			new_x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
			new_y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			new_color = (random.random(), random.random(), random.random())

			food.eat(new_x, new_y, color, 4)
			MY_BALL.r += 1
			MY_BALL.shapesize(MY_BALL.r/10)

	return True

def movearound(event):
	x = event.x - SCREEN_WIDTH
	y = SCREEN_HEIGHT - event.y

	MY_BALL.goto(x, y)
def AI(cur_ball):
	if(cur_ball.AI == 1):
		return False
	for dif_ball in BALLS:
		if(dif_ball.r > cur_ball.r):
			if check_near(cur_ball, dif_ball):
				cur_ball.changeDir(dif_ball.dx + 1, dif_ball.dy + 5)
				cur_ball.AI = 1
				return False

	for dif_ball in BALLS:
		if(dif_ball.r > cur_ball.r):
			if check_near(cur_ball, dif_ball):
				return False
	cur_ball.AI = 0
	return False
def check_near(ball_a, ball_b):
	D = math.sqrt(pow(ball_b.xcor() - ball_a.xcor(), 2) + pow(ball_b.ycor() - ball_a.ycor(), 2))
	if(D < 200):
		return True
	return False

'''
def threat():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if ball_a != ball_b:
				if(ball_a.r < ball_b.r):
					if(SCREEN_HEIGHT > 100 or -SCREEN_HEIGHT < 100 or SCREEN_WIDTH > 100 or -SCREEN_WIDTH < 100):
						D = math.sqrt(pow(ball_b.xcor() - ball_a.xcor(), 2) + pow(ball_b.ycor() - ball_a.ycor(), 2))
						if(D < 200):
							ball_a.changeDir(ball_b.dx + 1, ball_b.dy + 1)

	for ball_a in BALLS:
		for ball_b in BALLS:
			if ball_a != ball_b:
				if(ball_a.r < ball_b.r):
					D = math.sqrt(pow(ball_b.xcor() - ball_a.xcor(), 2) + pow(ball_b.ycor() - ball_a.ycor(), 2))
					if(D > 200):
						new_dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
						new_dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
						ball_a.changeDir(new_dx, new_dy)
'''

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()


while RUNNING:
	if(SCREEN_WIDTH == turtle.getcanvas().winfo_width()/2 or SCREEN_HEIGHT == turtle.getcanvas().winfo_height()/2):
		SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
		SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
		move_all_balls()
		check_collision()
		check_food_collision()
		check_myball_food()
		RUNNING = check_myball_collision()
		for ball in BALLS:
			AI(ball)
		turtle.update()
		time.sleep(SLEEP)

text = turtle.Turtle()
text.penup()
text.goto(-50, 0)
text.write("GAME OVER!", font=("Ariel", 20, "normal"))


turtle.mainloop()