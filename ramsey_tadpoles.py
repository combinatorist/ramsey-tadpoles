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
from itertools import product, groupby
from pprint import pprint
import tracemalloc
tracemalloc.start()

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

BruteStep = namedtuple(
    'BruteStep',
    [
      'step',
      'point'
    ]
)

def scan():
    # with open('./results.csv', 'w') as cache:
    modulo = 13
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
          has_min = has_min_chord or has_min_inverse
          has_max = has_max_chord or has_max_inverse
          has_easy_contradiction = is_coprime and has_min and has_max
          attempted_brute_residues = False

          if is_coprime and not has_easy_contradiction:
              # The trick here is to prove I can make a modulo cycle in red
              # ... but using diverse length red chords
              # Then, distinct combos of lengths would count as new chord to avoid.
              # Specifically, a sequence in red with as many steps as avoided in blue.
              # So, instead of multiplication, it's just repeated (diverse) addition.

              total_residues = get_brute_residues(modulo, generator, residues)
              brute_residues = [k for k, v in total_residues.items() if v.is_nontrivial]
              total_residues_plain = residues + brute_residues

              has_min_chord = j in(total_residues_plain)
              has_max_chord = k in(total_residues_plain)
              has_min_inverse = (modulo - j) in(total_residues_plain)
              has_max_inverse = (modulo - k) in(total_residues_plain)
              has_min = has_min_chord or has_min_inverse
              has_max = has_max_chord or has_max_inverse
              required_brute_residues = has_min and has_max
              attempted_brute_residues = True
          else:
              brute_residues = []
              required_brute_residues = False

          snapshot = tracemalloc.take_snapshot()
          top_stats = snapshot.statistics('lineno')
          pprint("[ Top 10 ]")
          pprint(top_stats[:10])

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
              1 if required_brute_residues else 0,
              1 if attempted_brute_residues else 0,
              "|".join(str(x) for x in residues),
              "|".join(str(x) for x in brute_residues)
          ]), flush=True)

StartResult = namedtuple('StartResult',
    [
       'has_started',
       'has_completed',
       'steps'
    ]
)

ResidueBelonging = namedtuple('ResidueBelonging',
    [
      'in_both',
      'is_nontrivial'
    ]
)

def preview_new_residues(modulo, steps, generator, residues):
    residues = {k: v._replace(is_nontrivial=False) for k,v in residues.items()}
    new_residues = get_n_length_residues(modulo, steps, generator)

    for i in new_residues:
        if not residues[i].in_both:
            residues[i] = ResidueBelonging(True, True)
    return {k:v for k,v in residues.items() if v.is_nontrivial}

def get_n_length_residues(modulo, steps, n):
    steps = [x.step for x in steps]
    num_steps = len(steps)
    if num_steps == modulo:
        simulated_cycle = steps + steps
        assert(n + num_steps < 2 * modulo)
        return set(sum(simulated_cycle[i:i+n]) % modulo for i in range(num_steps))
    else:
        return set(sum(steps[i:i+n]) % modulo for i in range(num_steps - n + 1))

def get_proper_residues(residues):
    return sorted([k for k, v in residues.items() if v.in_both])

def get_brute_residues(modulo, generator, residues=None):
    # "Starts" optimize and prioritize minimum non-trivial subsequences
    # ... so we don't have to check all possible (mostly redundant) sequences
    # We mill still redundantly check one start while working on another
    # ... but it still shouldn't be as bad as trying all possible sequences.
    if not residues:
        residues = get_residues(generator, modulo)
    if type(residues) is list:
        residues = {k: k in residues for k in range(modulo)}
        residues = {k: ResidueBelonging(v, False) for k,v in residues.items()}
    proper_residues = get_proper_residues(residues)

    def count_residues(rs):
        return len([r for r in rs.items() if r[1].in_both])

    #pprint(proper_residues)
    iterate = True
    while iterate:
        start_sequences = product(proper_residues, repeat=generator)
        normalized_starts = (sorted([v[::1], v[::1]])[0] for v in start_sequences)
        distinct_starts = set(normalized_starts)
        categorized_starts = {start: preview_new_residues(modulo, (BruteStep(x, 0) for x in start), generator, residues) for start in distinct_starts}
        promising_starts = {k: v for k,v in categorized_starts.items() if count_residues(v)}
        prioritized_starts = sorted(promising_starts.items(), key=lambda x: -count_residues(x[1]))

        #pprint('retrying with additional residues')
        iterate = False
        for start, effect in prioritized_starts:
            #pprint(start)
            result = test_start(modulo, residues, start)
            if result.has_completed:
                full_effect = preview_new_residues(modulo, result.steps, generator, residues)
                #pprint(full_effect)
                #pprint(result.steps)
                residues = {**residues, **full_effect}
                iterate = len([x for x in get_proper_residues(residues) if x != 0]) < modulo - 1
                break

    return residues

def test_start(modulo, residues, start):
    proper_residues = get_proper_residues(residues)
    point = 0
    points = [0]
    steps = []
    for x in start:
       point += x
       point %= modulo
       if point in points:
           # start is impossible
           return StartResult(False, False, steps)
       else:
           points.append(point)
           steps.append(BruteStep(x, point))

    has_started = True
    num_residues = len(proper_residues)
    max_residue = proper_residues[-1]
    residue_index = 0
    start_length = len(start)
    length = start_length

    while length < modulo:
       if residue_index == num_residues:
          # backtrack:
          #pprint('backtracking from:')
          #pprint(steps)
          if length <= start_length:
              return StartResult(has_started, False, steps)
          else:
              # backtrack
              step = steps.pop()
              while step.step == max_residue:
                 step = steps.pop()
              length = len(steps)
              points = [0] + [step.point for step in steps]

              point = points[-1]
              residue_index = proper_residues.index(step.step) + 1

       else:
          x = proper_residues[residue_index]

       new_point = (point + x) % modulo
       if new_point not in points or (new_point == 0 and length == modulo - 1):
           # add point to structure
           point = new_point
           points.append(point)
           steps.append(BruteStep(x, point))
           length += 1
           residue_index = 0
       else:
           # try next residue
           residue_index += 1
           continue

    return StartResult(has_started, True, steps)

if __name__ == '__main__':
    scan()
