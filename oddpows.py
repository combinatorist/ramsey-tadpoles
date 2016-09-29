# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 08:06:21 2014

@author: tperish
"""

def oddpows(evenpows, chord, modulus, printlist='default'):
    """Finds odd powers for a chord in a given mod. Enter evenpows as list"""
    oddpows = []
    for evenpow in evenpows:
        oddpows.append(evenpow * chord % modulus)

    if printlist in('default', True, 1,'yes'):
        print(oddpows)

    return(oddpows)
