# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 08:06:21 2014

@author: tperish
"""

def oddpows(evenpows, chord, modulus):
    """Finds odd powers for a chord in a given mod. Enter evenpows as list"""
    return [evenpow * chord % modulus for evenpow in evenpows]
