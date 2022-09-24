# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 08:12:08 2014

@author: combinatorist
"""

# outline
# 0. should output the format:
#         cntrd, chord1cntrd, chord2cntrd, note
# 1. check that both chords (i.e., their product) are relatively prime to p.
# 2. generate the even powers, watching for the chords to show up.
# 3. if either chord shows up, mark other chord found (by overlap contradiction)
# 4. if both chords were found, return overlap contradiction
# 5. now run odd powers for every chord not found.
# 6. if chord generates an even power or its inverse, mark it found, undirected
# 7. if both chords are found, mark complete
# 8. return contradictions found

# todo:
# * Optimize the contradiction finder and make a verbose explanation function.

from math import sqrt
from collections import namedtuple

def proof(chord1, chord2, modulus):
    """Find the first tadpole Ramsey number contradiction. Based on m-1, n-1"""

    #NB: Should I check that neither graph is a pan graph????
    generator = chord1 * chord2
    cntrd, chord1cntrd, chord2cntrd = False, False, False

    if not coprime(generator, modulus):
        note = 'chord product is not relatively prime to p'
        return cntrd, chord1cntrd, chord2cntrd, note

    evenpows = modpows(generator, modulus)
    # Find chord1 in evenpows to get contradiction for chord2 and vice versa
    chord2cntrd = evenpows.count(chord1) > 0
    chord1cntrd = evenpows.count(chord2) > 0

    overlapcntrds = [chord1cntrd, chord2cntrd].count(True)
    if overlapcntrds == 2:
        cntrd = True
        note = 'overlap contradiction'
        return cntrd, chord1cntrd, chord2cntrd, note

    eveninverses = modinverses(evenpows, modulus)
    evenchords = evenpows + eveninverses
    if not chord1cntrd:
        odd1pows = oddpows(evenpows, chord1, modulus)
        for power in odd1pows:
            if evenchords.count(power) > 0:
                chord1cntrd = True
    if not chord2cntrd:
        odd2pows = oddpows(evenpows, chord2, modulus)
        for power in odd2pows:
            if evenchords.count(power) > 0:
                chord2cntrd = True

    undredgcntrds = [chord1cntrd, chord2cntrd].count(True) - overlapcntrds
    note1 = str(overlapcntrds) + ' overlap contradict\'s, '
    note2 = str(undredgcntrds) + ' undirected edge contradict\'s'
    cntrd = chord1cntrd and chord2cntrd

    return cntrd, chord1cntrd, chord2cntrd, note1 + note2


def coprime(x, y):
    """checks that two integers are relatively prime"""

    small, big = min(x, y), max(x, y)
    iscoprime = True
    if small == 1:
        iscoprime = True
    elif big % small == 0:
        iscoprime = False
    else:
        for z in range(2, int(sqrt(small)) + 1):
            if small % z == 0:
                if big % z == 0 or big % (small / z) == 0:
                    iscoprime = False
                    break

    return iscoprime


def modpows(generator, modulus):
    """"Finds all powers of a generator in a given mod"""
    powers = []
    current = 1

    for _ in range(modulus):
        current = generator * current % modulus
        powers.append(current)
        if current in (1, 0):
            break

    return powers


def oddpows(evenpows, chord, modulus):
    """Finds odd powers for a chord in a given mod. Enter evenpows as list"""
    return [evenpow * chord % modulus for evenpow in evenpows]


def modinverses(values, modulus):
    """Finds the inverses in the modulus. Only takes normalized values."""
    return [modulus - value for value in values]

# Results = namedtuple(
#   'Result',
#   [
#     min_chord,
#     max_chord,
#     modulo,
#     is_primitive_root,
#     is_coprime,
#     has_min_chord,
#     has_min_inverse,
#     has_max_chord,
#     has_max_inverse,
#     residues
#   ]
# )

def get_residues(generator, modulo):
    residues = [1, generator]
    residue = generator * generator % modulo
    while residue not in residues:
        residues.append(residue)
        residue = residue * generator % modulo
    return residues

def scan():
    # with open('./results.csv', 'w') as cache:
    modulo = 3
    while True:
      modulo += 1
      max_chord = modulo - 2
      for j in range(2, max_chord + 1):
        for k in range(j, max_chord + 1):
          generator = (j * k) % modulo
          residues = get_residues(generator, modulo)
          is_primitive_root = len(residues) == modulo - 1
          nontrivial_residues = [x for x in residues[1:] if x != 0]
          is_coprime = is_primitive_root or (
              nontrivial_residues
                  and
              coprime(min(nontrivial_residues), modulo)
          )
          has_min_chord = is_primitive_root or j in(residues)
          has_max_chord = is_primitive_root or k in(residues)
          has_min_inverse = is_primitive_root or (modulo - j) in(residues)
          has_max_inverse = is_primitive_root or (modulo - k) in(residues)
          print(",".join(str(x) for x in [
              j,
              k,
              modulo,
              1 if is_primitive_root else 0,
              1 if is_coprime else 0,
              1 if has_min_chord else 0,
              1 if has_min_inverse else 0,
              1 if has_max_chord else 0,
              1 if has_max_inverse else 0,
              "|".join(str(x) for x in residues)
          ]))

StartResult = namedtuple(
    'StartResult',
    [
        has_started,
        has_completed,
        steps
    ]

ResidueBelonging = namedtuple(
    'ResidueBelonging',
    [
      in_left,
      in_right,
      is_nontrivial
    ]

def preview_new_residues(modulo, steps, j, k, residues):
    residues = {k: v.replace(is_nontrivial=False) for k,v in residues.items()}
    left = get_n_length_residues(modulo, steps, j)
    if j == k:
       right = left
    else:
       right = get_n_length_residues(modulo, steps, k)

    did_update = False
    for i in left:
        if not residues[i].in_left:
            other = residues[i].in_right
            residues[i] = ResidueBelonging(True, other, True)
    for i in right:
        if not residues[i].in_right:
            other = residues[i].in_right
            residues[i] = ResidueBelonging(other, True, True)
    return {k:v for k,v in residues.items() if v.is_nontrivial}

def get_n_length_residues(modulo, steps, n):
    return set(sum(cycle(x.step for x in steps)[i:i+n]) for i in range(modulo))

def new_residues_sort_key(rs):
    groups = groupby(sorted(rs, key=(lambda x: (x.in_left, x.in_right))))
    counts = (-len(x) for x in reverse(groups),)
    return counts

def get_brute_residues(modulo, j, k, residues=None):
    # "Starts" optimize and prioritize minimum non-trivial subsequences
    # ... so we don't have to check all possible (mostly redundant) sequences
    # We mill still redundantly check one start while working on another
    # ... but it still shouldn't be as bad as trying all possible sequences.
    if not residues:
        residues = get_residues(j * k, modulo)
    if type(residues) is list:
       residues = {k: k in residues for k in range(modulo)}
    start_sequences = product(residues, k)
    normalized_starts = (sorted(v, reverse(v))[0] for x in start_sequences)
    distinct_starts = set(normalized_starts)
    categorized_starts = (start: preview_new_residues(modulo, steps, j, k, residues) for start in distinct_starts)
    prioritized_starts = sorted(categorized_starts, key=lambda x: new_residues_sort_key(x[2]))

    for start, effect in prioritized_starts:
        result = test_start(modulo, residues, start)
        if result.has_completed:
            print(result)
            return get_brute_residues(modulo, j, k, residues | effect)

def test_start(modulo, residues, start):
    point = 0
    points = []
    steps = []
    for x in start:
       new_point += x % modulo
       if new_point in (points + 0):
           # start is impossible
           return StartResult(False, False, steps)
       else:
           point = new_point
           points.append(point)
           steps.append(BruteStep(x, point))

    has_started = True
    num_residues = len(residues)
    residue_index = 0
    start_length = len(start)
    length = start_length

    while length < modulo:
       if residue_index == num_residues:
          # backtrack:
          if length == start_length:
              return StartResult(has_started, False, steps)
          else:
              length -= 1
              steps.pop()
              points.pop()

              new_last_step = steps[-1]
              point = new_last_step.point
              residue_index = residues.index new_last_step.step + 1

       else:
          x = residues[residue_index]

       new_point += x % modulo
       if new_point in points:
          # try next residue
          residue_index += 1
          continue
       else:
           point = new_point
           points.append(point)
           steps.append(BruteStep(x, point))
           length += 1
           residue_index = 0

    return StartResult(has_started, True, steps)

if __name__ == '__main__':
    get_brute_residues(13, 2, 2)
