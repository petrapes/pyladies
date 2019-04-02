from turtle import *
from random import randint

shape('turtle')

color("Yellow")
bgcolor("MidnightBlue")
# star.color("yellow")

def randomplace():
	x = randint(-200,200)
	y = randint(-200,200)
	goto(x,y)

for stars in range(20):
	penup()
	randomplace()
	pendown()
	begin_fill()
	for star in range(5):
		forward(20)
		left(144)
		forward(20)
	right(72)
	end_fill()


hideturtle()
exitonclick()








