from turtle import *
from random import randrange

shape('turtle')

color("Yellow")
bgcolor("MidnightBlue")
# star.color("yellow")

for stars in range(1):
    begin_fill()
    for star in range(5):
        forward(20)
        left(144)
        forward(20)
    right(72)
    end_fill()
penup()
x = randrange(-200,200)
y = randrange(-200,200)
goto(y,x)
pendown()

for stars in range(1):
    begin_fill()
    for star in range(5):
        forward(20)
        left(144)
        forward(20)
    right(72)
    end_fill()


hideturtle()
exitonclick()








