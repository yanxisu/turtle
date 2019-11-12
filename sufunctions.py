import turtle
turtle.colormode(255)
b1 = turtle.Turtle()
b1.speed(0)

def tile(c):
    polygon(4,200,c)
    for times in range(4):
        polygon(3,100,"black")
        b1.forward(50)
        polygon(3,100,"black")
        b1.forward(50)
        polygon(3,100,"black")
        b1.forward(50)
        polygon(3,100,"black")
        b1.left(90)

def rowtile(c):
    for times in range(8):
        tile(c)
        b1.forward(200)

def spikeFlower(distance):
    for times in range(10):
        spike(distance)
        b1.penup()
        b1.home()
        b1.pendown()
        b1.left(times * 36)

def spike(distance):
    for times in range(20):
        c = times * 12
        b1.color(c,c,c)
        b1.width(times * 2)
        b1.forward(distance)
        b1.left(10)

def square(distance):
    for time in range(4):
        b1.forward(distance)
        b1.left(90)
        
def triangle(distance):
    for time in range(3):
        b1.forward(distance)
        b1.left(120)
        
def pentagon(distance):
    sides = 5
    angle = 360/ sides
    for times in range(sides):
        b1.forward(distance)
        b1.left(angle)
        
def polygon(sides, distance, c):
    b1.color(c)
    angle = 360/ sides
    b1.begin_fill()
    for times in range(sides):
        b1.forward(distance)
        b1.left(angle)
    b1.end_fill()
    
def jump(x,y):
    b1.penup()
    b1.goto(x,y)
    b1.pendown()

def star(distance,c):
    b1.color(c)
    b1.begin_fill()
    for times in range(5):
        b1.forward(distance)
        b1.left(144)
    b1.end_fill()

def explosion(distance,c):
    b1.color(c)
    b1.begin_fill()
    for times in range(8):
        b1.forward(distance)
        b1.left(72)
    b1.end_fill()

def figurel(distance,size,c):
    b1.begin_fill()
    b1.color(c)
    b1.circle(size)
    b1.forward(distance)
    b1.circle(size)
    b1.left(45)
    b1.forward(distance)
    b1.right(90)
    b1.forward(distance)
    b1.left(45)
    b1.circle(size)
    b1.forward(distance)
    b1.circle(size)
    b1.end_fill()

def monster(size,c):
    b1.begin_fill()
    b1.color(c)
    b1.lt(90)
    b1.fd(100)
    b1.circle(size)
    b1.lt(90)
    b1.fd(100)
    b1.lt(90)
    b1.fd(100)
    b1.lt(135)
    b1.fd(35)
    b1.rt(90)
    b1.fd(35)
    b1.lt(90)
    b1.fd(35)
    b1.rt(90)
    b1.fd(35)
    b1.end_fill()

def fadingTriangle():
    for times in range(500):
        c =(times * 2,times * 2,times * 2)
        polygon(3,450 - times * 2,c)

