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
from datetime import datetime, timedelta

from collections import namedtuple

ProofResult = namedtuple(
  "ProofResult",
  [
    'is_coprime',
    'is_upper_bound',
    'has_chord1_overlap_contradiction',
    'has_chord2_overlap_contradiction'])


def fast_proof(chord1, chord2, modulus):
    """Find all Diameter Ramsey number contradictions"""

    #NB: Should I check that neither graph is a pan graph????
    generator = chord1 * chord2 % modulus

    is_coprime = coprime(generator, modulus)



def proof(chord1, chord2, modulus):
    """Find the first tadpole Ramsey number contradiction. Based on m-1, n-1"""

    #NB: Should I check that neither graph is a pan graph????
    generator = chord1 * chord2
    cntrd, chord1cntrd, chord2cntrd = False, False, False

    is_coprime = coprime(generator, modulus)
    if not is_coprime:
        return cntrd, chord1cntrd, chord2cntrd

    evenpows = modpows(generator, modulus)
    # Find chord1 in evenpows to get contradiction for chord2 and vice versa
    has_chord2_overlap_contradiction = chord1 in evenpows
    if chord1 != chord2:
      has_chord1_overlap_contradiction = chord2 in evenpows
    else:
      has_chord1_overlap_contradiction = has_chord2_overlap_contradiction

    eveninverses = modinverses(evenpows, modulus)
    evenchords = evenpows + eveninverses
    odd1pows = oddpows(evenpows, chord1, modulus)
    has_chord1_inverse_contradiction = False
    for power in odd1pows:
        if evenchords.count(power) > 0:
            has_chord1_inverse_contradiction = True
            break
    has_chord2_inverse_contradiction = False
    for power in odd1pows:
        if evenchords.count(power) > 0:
            has_chord2_inverse_contradiction = True
            break

    return cntrd, chord1cntrd, chord2cntrd, note1 + note2


def coprime(x, y):
    """checks that two integers are relatively prime"""

    small, big = min(x, y), max(x, y)
    iscoprime = True
    if big % small == 0:
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


class Logger:
  def __init__(self):
      self.last_log_time = datetime.now()

  def log(self, content, check=False):
      now = datetime.now()
      if not check or now - self.last_log_time > timedelta(seconds = 10):
        print("")
        print(now.isoformat() + ": \n" + str(content))
        self.last_log_time = now

logger = Logger()

def scan(scale_start=2, diff_start=0, ceil_start=2):
    i = scale_start
    j = diff_start
    k = ceil_start
    max_k = 2
    max_k_list = []
    max_k_ratio = 1
    max_k_ratio_list = []
    while True:
      while j <= i:
        while True:
          J = i + j
          K = J + k
          res = proof(i, J, K)
          if res[0]:
            k_ratio = 1.0 * K / J
            if k_ratio > max_k_ratio:
              max_k_ratio = k_ratio
              max_k_ratio_stats = ((i, 1.0 * J / i, J, k_ratio, K), res)
              max_k_ratio_list += max_k_ratio_stats
              logger.log(("new max k ratio:", max_k_ratio_stats))
              # logger.log(modpows(i * J, K))
            if k > max_k:
              max_k = k
              max_k_stats = ((i, j, J, k, K), res)
              max_k_list += max_k_stats
              logger.log(("new max k:", max_k_stats))
              # logger.log(modpows(i * J, K))
            break
          logger.log((i, J, K), check = True)
          k += 1
        j += 1
        k = 2
      i += 1
      j = 0

def counters(max=4, a=2, b=2):
    while 
if __name__ == "__main__":
   scan()
