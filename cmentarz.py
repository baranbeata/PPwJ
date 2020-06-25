# -*- coding: utf-8 -*-
import turtle
import math

global zolwik
zolwik = turtle.Turtle()

def kwartal(n, m):
    k=[]
    for i in range(n):
        x=[]
        for j in range(m):
            x.append(None)
        k.append(x)
    return k


#k = kwartal(4, 3)
#print(k)

def maszyna(k, *arg):
    #arg w postaci par współrzędnych
    for i in range(0, len(arg), 2):
        if k[arg[i]][arg[i+1]] == None:
            k[arg[i]][arg[i+1]] = {}
        else:
            pass

#maszyna(k, 1, 1, 2, 1, 1, 2, 1, 1)
#print(k)

def pochowaj_r(k, *arg):
    #arg w postaci trójek: x, y, ilosc ramion
    for i in range(0, len(arg), 3):
        if (k[arg[i]][arg[i+1]] == {}):
            nowy_zwierz = {"Ilosc ramion" : arg[i+2]}
            r = {"rodzaj": "rozgwiazda"}
            k[arg[i]][arg[i+1]].update(nowy_zwierz)
            k[arg[i]][arg[i+1]].update(r)
        else:
            pass

def pochowaj_a(k, *arg):
    #arg w postaci czwórek: x, y, srednica muszli, ilosc zwojow
    for i in range(0, len(arg), 4):
        if (k[arg[i]][arg[i+1]] == {}):
            nowy_zwierz = {"Srednica muszli" : arg[i+3], "Ilosc zwojow": arg[i+2]}
            r = {'rodzaj': 'amonit'}
            k[arg[i]][arg[i+1]].update(nowy_zwierz)
            k[arg[i]][arg[i+1]].update(r)
        else:
            pass

def zakop_r (k, x, y, *, ilosc_ramion, **arg):
    if (k[x][y] == {}):
        nowy_zwierz = arg
        ramiona = {"Ilosc ramion" : ilosc_ramion }
        nowy_zwierz.update(ramiona)
        r = {'rodzaj': 'rozgwiazda'}
        nowy_zwierz.update(r)
        k[x][y].update(nowy_zwierz)
    else:
        pass
    
    
 



#pochowaj_r(k, 1, 1, 5, 0, 0, 4)
#print(k)

#pochowaj_a(k, 2, 1, 10, 5, 1, 2, 5, 5)
#print(k)

def wiz_kwatery():
    pass


def wiz_kwartalu(k):
    #ilość wierszy
    row = len(k)
    #ilość kolumn
    col = len(k[0])

    #szerokosc kwatery
    k_width = 100
    #wysokosc kwatery
    k_height = 150

    #szerokosc kwartalu
    width = col * k_width
    #wysokosc kwartalu
    height = row * k_height

    #lewy górny róg
    up_left = (-(width/2), height/2)

    global zolwik

    
    
    #zolwik = turtle.Turtle()

    zolwik.speed(0)
    
    zolwik.penup()
    zolwik.goto(up_left)
    zolwik.pendown()
    zolwik.setheading(0)

    w = 0
    for i in range(row):
        for j in range(col):
            zolwik.forward(k_width)
            zolwik.right(90)
            zolwik.forward(k_height)
            zolwik.right(90)
            zolwik.forward(k_width)
            zolwik.right(90)
            zolwik.forward(k_height)
            zolwik.right(90)
            zolwik.forward(k_width)
        w = w + 1
        zolwik.penup()
        zolwik.goto(-(width/2), (height/2)-w*k_height)
        zolwik.pendown()
    
    #wiz_rozgwiazda(0, 0, 5, 20)

    cx = -(width/2) + k_width/2
    cy = height/2 - k_height/2

    g = 0;
    
    for i in range(row):
        p = 0
        for j in range(col):
            if k[i][j] == None:
                zolwik.penup()
                zolwik.goto((cx + p*k_width), (cy - g*k_height))
            elif k[i][j] == {}:
                zolwik.penup()
                zolwik.goto((cx + p*k_width), (cy - g*k_height))                
            elif k[i][j]['rodzaj'] == 'rozgwiazda':
                wiz_rozgwiazda((cx + p*k_width), (cy - g*k_height), k[i][j]["Ilosc ramion"], 40)
            elif k[i][j]['rodzaj'] == 'amonit':
                wiz_amonit((cx + p*k_width), (cy - g*k_height), k[i][j]["Ilosc zwojow"], k[i][j]["Srednica muszli"])
            else:
                zolwik.penup()
                zolwik.goto((cx + p*k_width), (cy - g*k_height))
            p = p + 1
        g = g + 1


def wiz_rozgwiazda(x, y, r, s):

    global zolwik

    #zolwik = turtle.Turtle()

    zolwik.speed(0)
    
    zolwik.penup()
    zolwik.goto(x, y)
    zolwik.pendown()

    angle = 360 / r
    
    for i in range(0, r):
        zolwik.forward(s)
        zolwik.penup()
        zolwik.backward(s)
        zolwik.left(angle)
        zolwik.pendown()

    zolwik.penup()


def wiz_amonit(x, y, z, s):

    global zolwik

    #zolwik = turtle.Turtle()

    zolwik.speed(0)
    
    zolwik.penup()
    zolwik.goto(x, y)
    zolwik.pendown()
    size=s

    zolwik.setheading(90) #Point the top
    zolwik.forward(size)
    zolwik.setheading(215) #Point the left
    newSize=size
    newSize = (newSize*(math.sqrt(3)/2)) / math.sin(math.radians(65))
    for i in range(0,z):  
        zolwik.forward(newSize)
        zolwik.left(60)
        newSize = (newSize*(math.sqrt(3)/2)) / math.sin(math.radians(70))

    zolwik.penup()

def statystyki(k):
    
    #ilość wierszy
    row = len(k)
    #ilość kolumn
    col = len(k[0])

    puste = 0
    rozgwiazdy = 0
    amonity = 0
    rozkopane = 0
    
    for i in range(row):
        for j in range(col):
            if k[i][j] == None:
                puste = puste + 1
            elif k[i][j] == {}:
                rozkopane = rozkopane + 1
            elif k[i][j]['rodzaj'] == 'rozgwiazda':
                rozgwiazdy = rozgwiazdy + 1
            elif k[i][j]['rodzaj'] == 'amonit':
                amonity = amonity + 1

    stat = { "Wolnych miejsc" : puste, "Rozgwiazd" : rozgwiazdy, "Amonitow": amonity, "Rozkopanych" : rozkopane }
    return stat
    


if __name__ == '__main__':
    k = kwartal(4, 4)
    #print(k)
    maszyna(k, 0, 0, 1, 1, 2, 1, 1, 2, 1, 1, 3, 3, 2, 2, 2, 3)
    #print(k)
    pochowaj_r(k, 1, 1, 5, 0, 0, 6, 3, 3, 5, 2, 3, 7)
    #zakop_r(k, 1, 1, ilosc_ramion=5, Imie="Basia")
    #print(k)

    pochowaj_a(k, 2, 1, 12, 25, 1, 2, 24, 40, 2, 2, 24, 44)
    print(k)

    wiz_kwartalu(k)

    staty = statystyki(k)
    print(staty)

    #wiz_rozgwiazda(0, 0, 5, 40)
    
    #wiz_amonit(0, 0, 24, 35)
    
