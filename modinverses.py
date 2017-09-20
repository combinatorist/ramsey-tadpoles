# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 08:11:16 2014

@author: tperish
"""

def modinverses(values, modulus):
    """Finds the inverses in the modulus. Only takes normalized values."""
    return [modulus - value for value in values]
