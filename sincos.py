import math
import turtle

a = range(-25, 26)

l = [(x, y) for x in a for y in a]

f = lambda x, y : math.sin(x)*math.cos(y)

skala = lambda a : a * 2 * math.pi /25

skalowane = [ tuple(map(skala, i)) for i in l]

#print (skalowane)

obliczone = [ f(i[0], i[1]) for i in skalowane]

zipped = list(zip (l, obliczone))

#print (obliczone)
print (zipped)


zolwik = turtle.Turtle()
zolwik.speed(0)

#colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 

x = 0

for i in zipped:
    #print(i[0][0], i[0][1])
    #zolwik.pencolor(colors[x%6])
    zolwik.penup()
    zolwik.goto(i[0][0]*10, i[0][1]*10+i[1])
    zolwik.pendown()
    zolwik.circle(i[1]*5)
    x+=1
    
