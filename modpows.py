# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 08:05:30 2014

@author: tperish
"""

def modpows(generator, modulus, printlist='default'):
    """"Finds all powers of a generator in a given mod"""
    powers = []
    current = 1

    for _ in range(modulus):
        current = generator * current % modulus
        powers.append(current)
        if current in (1, 0):
            break
    if printlist not in('default', False, 0, 'No'):
        print(powers)
    return powers
