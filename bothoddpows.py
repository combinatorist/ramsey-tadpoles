# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 08:06:55 2014

@author: tperish
"""
import modpows
import oddpows

def bothoddpows(chord1,chord2,modulus,printlist = 'default'):
    """print both sets of odd powers"""

    evenpows = modpows(chord1 * chord2, modulus)
    oddpows1 = oddpows(evenpows,chord1,modulus,printlist = False)
    oddpows2 = oddpows(evenpows,chord2,modulus,printlist = False)

    print(oddpows1)
    oddpows1.sort()
    print(oddpows1)
    
    print(oddpows2)  
    oddpows2.sort()
    print(oddpows2)

    evenpows.sort()
    print(evenpows)