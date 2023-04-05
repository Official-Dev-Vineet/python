import turtle
t=turtle.Turtle()

for x in range(1,99):
    t.color('red')
    t.left(40*x)
    t.circle(x*5)
    t.forward(40*x)
    t.right(30*x)
    