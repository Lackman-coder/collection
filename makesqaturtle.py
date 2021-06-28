import turtle
 
t = turtle.Turtle()
t.fillcolor('red')
t.begin_fill()
for i in range(4):
  t.forward(150)
  t.right(90)
t.end_fill()
f  = turtle.Turtle()
f.fillcolor("blue")
f.begin_fill()
for j in range(3):
	f.forward(100)
	f.left(150)
	f.forward(100)
f.end_fill()
g = turtle.Turtle()
g.fillcolor("green")
g.begin_fill()
g.circle(80)
g.end_fill()