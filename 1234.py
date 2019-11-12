from sufunctions import *

turtle.colormode(255)
turtle.bgcolor("black")
b1.speed(0)

for times in range(100):
    c =(250-times * 2, 0 ,250-times * 2)
    b1.color(c)
    b1.fd(times * 12)
    b1.lt(179)
    c =(0, 250 - times * 2 ,0)
    b1.color(c)
    b1.circle(times * 2)

jump(0,0)
for times in range(100):
    c =(0, 250 - times * 2 ,250-times * 2)
    b1.color(c)
    b1.fd(times * 12)
    b1.rt(179)
    c =(0, 250 - times * 2 ,0)
    b1.color(c)
    b1.circle(times * 2)

jump(0,0)
for times in range(100):
    c =(0, 250 - times * 2 ,250-times * 2)
    b1.color(c)
    b1.fd(times * 12)
    b1.lt(145)


jump(0,0)
for times in range(100):
    c =(250-times * 2, 0 ,250-times * 2)
    b1.color(c)
    b1.fd(times * 12)
    b1.rt(145)



