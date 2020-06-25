import turtle
import math
import random

def point(x, y, R, ang):
    ang = math.radians(ang)
    xp = x + R * math.cos(ang)
    yp = y + R * math.sin(ang)

    return (xp, yp)

pkt = point(2, 2, 4, 30)
#print(pkt)

def generatePoints(x, y, R, k):

    n = int(360/k)

    for i in range(n):
        res = point(x, y, R, i*k)

        yield res


points = generatePoints(0, 0, 100, 30)
other_points = generatePoints(-200, -100, 80, 20)
last_points = generatePoints(200, -100, 80, 60)


def draw(cir, fi):
    turtle.penup()
    turtle.goto(cir[0], cir[1])
    turtle.pendown()
    turtle.colormode(255)
    turtle.begin_fill()
    turtle.fillcolor(random.randrange(255), random.randrange(255), random.randrange(255))
    turtle.circle(fi)
    turtle.end_fill()

for i in points:
    draw(i, 5)

for i in other_points:
    draw(i, 6)

for i in last_points:
    draw(i, 8)
