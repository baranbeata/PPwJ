#1. Symbol Newtona wyliczany w sposob funkcyjny
#2. Funkcja generujaca funkcje: wielomian Bernsteina
#   parametry: u, i
#3. Funkcja generujaca funkcje wyliczjaca punkt na krzywej Beziera
#   parametry: sekwencja punktow kontrolnych
#   parametr funkcji wewnetrznej: t \in [0, 1]
#4. Funkcja dostarczajaca generator w postaci wyrazenia generatorowego,
#generator ma dostaczac kolejne punkty na krzywej Beziera
#   parametr: ilosc punktow

from math import factorial

#***NEWTON***

def Newton(n, k):
    try:
        res = factorial(n)/(factorial(k)*(factorial(n-k)))
        return res
    except ValueError:
        print('ERROR Nieprawidlowe wartosci wejsciowe')

a = Newton(8, 6)
print (a)

#***BERNSTEIN***

def generateBernstein(u, i):
    try:
        if i < 0 or i > u:
            yield 0
        else:
            def Bernstein(t):
                yield (Newton(u, i)*t**i*((1-t)**(u-i)))
            yield Bernstein
                
    except ValueError:
        print('ERROR Nieprawidlowe wartosci wejsciowe')

b = generateBernstein(4, 2)

print(b)

for i in b:
    print (i)
    print (i(2))
    for j in i(2):
        print (j)


#***BEZIER***

def generateBezier():
    def Bezier(p1, p2, p3, p4, t):
        x = (1 - t)**3*p1[0]+3*(1 - t)**2*t*p2[0]+3*(1 - t)*t**2*p3[0]+t**3*p4[0]
        y = (1 - t)**3*p1[1]+3*(1 - t)**2*t*p2[1]+3*(1 - t)*t**2*p3[1]+t**3*p4[1]
        z = (1 - t)**3*p1[2]+3*(1 - t)**2*t*p2[2]+3*(1 - t)*t**2*p3[2]+t**3*p4[2]
        p = (x, y, z)
        yield(p)
    yield Bezier

bez = generateBezier()

for p in bez:
    print(p)
    for k in p((1,1,1), (1,2,1), (2,2,1), (1,2,2), 0.5):
        print (k)

def generateBezierPoints(n):
    k = 1/(n-1)
    pts = (i*k for i in range(n))
    def BezierPoints(p1, p2, p3, p4):
        gen = generateBezier()
        #res = (gen(p1, p2, p3, p4, t) for t in pts)
        yield gen
    yield BezierPoints


bp = generateBezierPoints(5)

##for l in bp:
##    print (l)
##    for m in l((1,1,1), (1,2,1), (2,2,1), (1,2,2)):
##        for n in m:
##            print (n)
        

    

#((1,1,1), (1,2,1), (2,2,1), (1,2,2))

