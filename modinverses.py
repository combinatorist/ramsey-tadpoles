# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 08:11:16 2014

@author: tperish
"""

def modinverses(values, modulus):
    """Finds the inverses in the modulus. Only takes normalized values."""

    inverses = []
    for value in values:
        inverses.append(modulus - value)    #use value between 0 and modulus

    return(inverses)