Ramsey Tadpoles Python Module Spec
==================================
Tim Perisho
10/17

## Classes
- Tadpoles
- Tadpole pairs
- Cycle size pairs

## Functions
- trivial_lb - Determine trivial LB for arbitrary graphs
- rcmcn - Determine ramsey numbers for cycle graph pairs
  - Input: 2 integers representing cycle sizes
  - Output: 1 integer representing ramsey number
- Diagonal cases, list powers
- Diagonal cases, check powers
  - Whether it has odd or even order. (output: even order)
  - Whether it has add. Inverses. (output: even order w/o add. inverses)
  - Whether it -1 is an odd power. (output: odd, even power to -1)
- Diagonal sampling 1
  - For each cycle size, find first p that gives contradiction
- efficiently check for a contradiction given two tadpole graphs
  - Input: 2 tadpoles (each is a two integer tuple)
  - Output: either not rel. prime (graph 1,2), or no such contradiction
- efficiently find the first p with a contradiction given two cycle sizes.
  - Find first p coprime to 2 numbers
- Give Lower and Upper Bounds
  - Perhaps compare to trivial LB to see if it’s exact or give range.
  - Alt. output: give LB, UB, and notice about where UB was found
  - \*Notice, I’ll need both the lower bouond of the inputed tadpoles and the lower bound of the found contradiction.
