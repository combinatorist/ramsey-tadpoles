# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 08:08:43 2014

@author: tperish
"""
from math import sqrt

def coprime(x, y):
    """checks that two integers are relatively prime"""

    small, big = min(x, y), max(x, y)
    iscoprime = True
    if big % small == 0:
        iscoprime = False
    else:
        for z in range(2, int(sqrt(small)) + 1):
            print(z)
            if small % z == 0:
                print 'small'
                if big % z == 0 or big % (small / z) == 0:
                    iscoprime = False
                    break

    return(iscoprime)
