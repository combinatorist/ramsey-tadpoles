# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 08:06:55 2014

@author: tperish
"""
from modpows import modpows
from oddpows import oddpows

def bothoddpows(chord1, chord2, modulus):
    """return both sets of odd powers"""

    evenpows = modpows(chord1 * chord2, modulus)
    oddpows1 = oddpows(evenpows, chord1, modulus)
    oddpows2 = oddpows(evenpows, chord2, modulus)

    return (oddpows1, oddpows1.sort(), oddpows2, oddpows2.sort(), evenpows,
        evenpows.sort())
