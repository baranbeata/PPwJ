# -*- coding: utf-8 -*-

import sys
import math

res = []

for i in range(2, 81):
    res.append(i)
    
def sito(res):
    for j in res:
        for k in res:
            if k <= j:
                continue
            elif k%j == 0:
                res.remove(k)
        if j > math.sqrt(res[-1]):
            break
        
    return res

if __name__ == '__main__':
    try:
        if int(sys.argv[1]) > 20:
            print('Podano pierwsze 20 liczb')
        print (sito(res)[0:int(sys.argv[1])])
    except ValueError:
        print('Podano zla wartosc')
    
            
