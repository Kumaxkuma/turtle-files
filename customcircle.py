import turtle


while True:
	screen = turtle.getscreen()
	squirtle = turtle.Turtle()
	squirtle.pencolor("green")
	squirtle.fillcolor("teal")
	squirtle.pensize(5)
	squirtle.speed(5)
	squirtle.begin_fill()
	squirtle.circle(110)
	turtle.bgcolor("purple")
	squirtle.end_fill()