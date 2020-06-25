# -*- coding: cp1250 -*-

def euklides(a, b):
    
    i = 0

    if ( a > b ):
        while( a >= b ):
            i = i + 1
            a = a - b
        b = a
    else:
        while ( b >= a ):
            i = i + 1
            b = b - a
        a = b 
   
    return i, a

if __name__ == '__main__':
    while(True):
        try:
            x = eval(input('Proszę podać pierwszą liczbę: '))
            y = eval(input('Proszę podać drugą liczbę: '))
            x = int(x)
            y = int(y)
            break
        except (NameError, ValueError, TypeError):
            print ('ERROR: Proszę podać liczbę całkowitą\n')
        
    res = euklides(x, y)
    print ('Wynik dzielenia: ' + str(res[0]), ' Reszta: ' +  str(res[1]))


