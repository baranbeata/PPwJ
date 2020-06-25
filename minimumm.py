import math
import itertools

#funkcja ma zwracać ARGUMENTY,
#dla których osiąga minimum

Q = range(20)

f = lambda a, b, c, d : (math.sin(a)*b)/(c+math.cos(d))

def funkcja(Q):
    a = itertools.combinations(Q, 4)
    #print(list(a))

    wyniki = []

    for i in a:
        #print (f(i[0], i[1], i[2], i[3]))
        wyniki.append(f(*i)) # * rozpakowuje argumenty!

    print (min(wyniki))

funkcja(Q)

def g(* ll):
    if not ll: return []
    if len(ll) == 1:
        return [(e,) for e in ll[0]]
    else:
        L = []
        for post in g(*ll[1:]):
            for pre in ll[0]:
                L.append((pre,)+post)
        return g(L)

print (g((1,), (2,), (3,), (4,), (5,), (6,)))
