import turtle

s = turtle.getscreen()
t = turtle.Turtle()


t.right(90)
t.forward(100)
t.left(90)
t.backward(100)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
turtle.exitonclick() # will not close the window
# shorter version
# t.rt() instead of t.right()
# t.fd() instead of t.forward()
# t.lt() instead of t.left()
# t.bk() instead of t.backward()

t.setposition(0,60)

t.goto(100,100)
t.home() # mouse will go home
t.circle(60)
t.dot(20)

c = t.clone()#will clone
    #t.color("magenta")
    #c.color("red")
    #t.circle(100)
    #c.circle(60)

turtle.bgcolor("blue") #-> background color
t.color('red') # turtle color / t.pencolor

t.fillcolor('green')
t.begin_fill
t.end_fill

turtle.title("My Turtle Program") # change title
t.hideturtle() # turtle will dissapear
t.pensize(20) # change size of line
t.shape("turtle")/("arrow")/("circle")#chg shape of turtleSquare(Triangle,Classic)

t.undo() #undo
t.clear()#clear
t.reset()

t.stamp() #will leave turtle stamp

#=====FOR_LOOP==========
for i in range(4):
     t.fd(100)
     t.rt(90)


#https://docs.python.org/3/library/turtle.html
#https://realpython.com/beginners-guide-python-turtle/


#EX: Olimpic rings
import turtle as t
t.hideturtle()
def draw_circle(x,y,color):
    t.pensize(10)
    t.color(color)
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.circle(30)
draw_circle(60,0,'blue')
draw_circle(-15,0,'purple')
draw_circle(90,40,'red')
draw_circle(15,40,'yellow')
draw_circle(-60,40,'green')
t.exitonclick()