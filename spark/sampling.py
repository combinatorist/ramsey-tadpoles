#!/usr/bin/env python3

from os import system
from sys import argv
from math import log2

def run(starting_max_modulo=31, starting_min_modulo=31, starting_modulo=31):
  max_modulo = starting_max_modulo
  min_modulo = starting_min_modulo
  is_start = True

  while True:
    if not is_start:
      starting_modulo = min_modulo
    else:
      is_start = False
    for modulo in range(starting_modulo, max_modulo + 1):
      print(f'running with ${(max_modulo, min_modulo, modulo)}')
      system(f'spark-submit --class Main target/scala-2.13/spark-ramsey-numbers_2.13-0.1.jar ${modulo}')
    if log2(max_modulo) % 1 == 0:
      min_modulo += 1
    max_modulo += 1

if __name__ == '__main__':
  args = [int(a) for a in argv[1:]]
  print(args)
  run(*args)
