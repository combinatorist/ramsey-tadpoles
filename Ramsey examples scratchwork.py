#This is a module from scratch to help with Ramsey numbers
from math import sqrt

def modpows(generator, modulus, printlist = 'default'):
    """"Finds all powers of a generator in a given mod"""
    powers = []
    current = 1

    for x in range(modulus):
        current = generator * current % modulus
        powers.append(current)
        if current == 1:
            break
    if printlist not in('default',False,0,'No'):
        print(powers)
    return(powers)

def oddpows(evenpows, chord, modulus, printlist = 'default'):
    """Finds odd powers for a chord in a given mod. Enter evenpows as list"""
    oddpows = []
    for evenpow in evenpows:
        oddpows.append(evenpow * chord % modulus)

    if printlist in('default',True,1,'yes'):
        print(oddpows)

    return(oddpows)

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


#Here's where it gets serious
def coprime(x, y):
    """checks that two integers are relatively prime"""

    small, big = min(x, y), max(x, y)
    iscoprime = False
    for z in range(2, int(sqrt(small)) + 1):
        print(z)
        if small % z == 0:
            if big % z == 0 or big % (small / z) == 0:
                iscoprime = True
                break

    return(iscoprime)

def modinverses(values, modulus):
    """Finds the inverses in the modulus. Only takes normalized values."""

    inverses = []
    for value in values:
        inverses.append(modulus - value)    #use value between 0 and modulus

    return(inverses)

def tadpole(chord1, chord2, modulus):
    """Find the first tadpole Ramsey number contradiction. Based on m-1, n-1"""

#Shouldn't I build something in to check that neither graph is a pan graph????
    generator = chord1 * chord2
    cntrd, chord1cntrd, chord2cntrd = False, False, False

    if coprime(generator, modulus):
        note = 'chord product is not relatively prime to p'
        return(cntrd, chord1cntrd, chord2cntrd, note)

    evenpows = modpows(generator, modulus)
    print(evenpows)
    if evenpows.count(chord1) > 0:
        chord2cntrd = True  #Yes, find chord1 to get contradiction for chord2
    if evenpows.count(chord2) > 0:
        chord1cntrd = True

    overlapcntrds = [chord1cntrd, chord2cntrd].count(True)
    if overlapcntrds == 2:
        cntrd = True
        note = 'overlap contradiction'
        return(cntrd, chord1cntrd, chord2cntrd, note)

    eveninverses = modinverses(evenpows, modulus)
    print(eveninverses)
    evenchords = evenpows + eveninverses
    if not chord1cntrd:
        print('chord1 odd powers')
        odd1pows = oddpows(evenpows,chord1,modulus,printlist = True)
        for pow in odd1pows:
            if evenchords.count(pow) > 0:
                chord1cntrd = True
    if not chord2cntrd:
        print('chord2 odd powers')
        odd2pows = oddpows(evenpows,chord2,modulus,printlist = True)
        for pow in odd2pows:
            if evenchords.count(pow) > 0:
                chord2cntrd = True

    undredgcntrds = [chord1cntrd, chord2cntrd].count(True) - overlapcntrds
    note1 = str(overlapcntrds) + ' overlap contradict\'s, '
    note2 = str(undredgcntrds) + ' undirected edge contradict\'s'
    cntrd = chord1cntrd and chord2cntrd

    return(cntrd, chord1cntrd, chord2cntrd, note1 + note2)


'''outline
0. should output the format:
        cntrd, chord1cntrd, chord2cntrd, note
1. check that both chords (i.e., their product) is relatively prime to p.
2. generate the even powers, watching for the chords to show up.
3. if either chord shows up, mark other chord as found in overlap contradiction
4. if both chords were found, return overlap contradiction
5. now run odd powers for every chord not found.
6. if chord generates an even power or its inverse, mark it found, undirected
7. if both chords are found, mark complete
8. return contradictions found
'''

#Optimize the contradiction finder and make a verbose explanation function.
