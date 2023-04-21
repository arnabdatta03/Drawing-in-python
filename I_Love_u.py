import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.hideturtle()
t.goto(0,-10)

turtle.pensize(3)
t.color('red')
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(178)
t.end_fill()

t.penup()
t.goto(-75,130)
t.pendown()
t.color('red')
t.write("ARNAB",font=("chiller",30,"bold"))


t.penup()
t.goto(-220,-180)
t.pendown()
t.color('white')
t.write("I LOVE U",font=("verdana",30," "))
a=input()


turtle.done()