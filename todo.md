Oh my goard! Just realized with mixed chord-length cycles, the chord lengths no longer need to be coprime!

Shit! It's totally recursive:
1. I've been using the symmetric generator for the number of mixed length steps to count
1. So, for example, suppose I'm avoiding mixed lengths in red.
1. Then, I want a red-steps linear combination of those mixed lengths.
1. And then, I have been looking for a blue-length product of that red-avoided blue-chord./
1. But, its actually a blue-length linear combination of those those red-avoided chords with other blue chords
1. In other words, I find a new red-avoided blue chord length, but then return to the same simple multiplication in avoiding blue.
1. ... when instead, I should be considering mixed combinations in blue (including the new blue-chord) too on top of red.
1. I think I though I was handling this with multiplication, because there's a symmetry when I switch red and blue
1. ... but that symmetry of multiplication does not cover the twice over linear combinations.

... but, actually I am, because in the code, I multiply red and blue to the number of steps and then apply that to linear combinations.
My concern above only holds if I were getting the linear combinations for red and then simply multiplying by blue, but with red*blue, I capture all possible linear combinations, not just the repeated sequence of red chords making up the same repeated blue chord.


1. do I represent as inverses or large residues or both?
1. is there anywhere I can't "subtract" (even in undirected graphs)?
1. it should be ok to negate my mixed lengths step product (red*blue) at least for undirected graphs
1. of course it would be the absolute value for the number of steps
1. so I could use this to find the smaller number of steps to consider (fewer input possibilities)
1. but I also need to eplicitly allow negated input residues chord lengths (for undirected graphs) or I won't get any "twists"!
1. but is it be ok to reduce my mixed lengths step product (red*blue) with the modulo? that would speed things up!
1. yes! simple argument:
1. suppose I need 3 and 5 mod 11 to get me a chord of 2 (with some input predetermined residues)
1. then, if I can make a valid cycle with 4 steps of those residues, then I can easily construct one in 15 steps by adding a lap

1. notice non-trivial brs only seem to occur on symmetric cases, maybe that has something to do with directed input residues
1. do I need one-sided residues (only matching min or max chord) help to build up to a two-sided (like with a linear combination or something)?
1. consider autogenerating plus/minus residues for standardization or even more completeness (i.e. consider +/- on residue side instead of chord side)

1. handle that residues sometimes end on a redundant 1
1. write csv efficiently in chunks
1. read and initialize with csv (rather than creating starting point arguments)
1. consider speeding up implicit modpows in scan function
1. don't recompute residues for pairs of factors that make the same generator
1. handle inverses already computed

