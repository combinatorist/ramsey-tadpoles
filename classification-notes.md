My generated graph colorings (e.g. red lines after simple calculating simple generated residues) are Cayley Graphs (https://en.wikipedia.org/wiki/Cayley_graph)
for the cyclic group Cn (https://en.wikipedia.org/wiki/Cyclic_group#Cayley_graph).

In other words, it is a circulant graph: (https://en.wikipedia.org/wiki/Circulant_graph#:~:text=The%20graph%20is%20a%20Cayley%20graph%20of%20a%20cyclic%20group.)
Specifically, only circulant graphs where the generating subset S are the powers of another generator (the product of the 2 chord lengths), which are also coprime to n).

So, put another way, I'm looking for novel (i.e. non-trivial, or mixed chord length)
cycle Cn subgraphs of these specific ("generated") circulant graphs.

... to see what other chord lengths I can generate for avoidance.

... but once I find some novel chord lengths to avoid, then I'm looking at circulant graphs from more complicated generating sets.

I'm not sure it's even possible to exclude a class of circulant graphs (without defining it post hoc, directly in terms of my needs).

I think I could say it could include any Circulant based on a (additively) generating set S which is in turn based on a finite set of (multiplicative) generators.
However, since we're considering finite cycles, would this include every S?

No, actually - simply leave out some higher or lower powers of the multiplicative generators (chord product) and that's not really a graph I'm interested in.

In theory, I could sometimes get a non-trivial result from just some of the powers (via a non-trivial, mixed chord-length cycle), but there's no reason I would throw away the other powers when they're so easy to compute.

So, yeah, if it helps, I can fous on the (multiplicatively) generated (additively) generating sets.
(Is this just a ring)?


[BTW, it likely also gets complicated if we switch to directed graphs. Then, it's still Cayleys, but not circulants.]
[Also, FWIW, I think when they are undirected, these Cayleys also count as a symmetric graphs (https://en.wikipedia.org/wiki/Symmetric_graph)
 ... although, I haven't proved the edge-transitivity yet.]

This is helpful, because Sage has several ways to construct circulant graphs:
- https://doc.sagemath.org/html/en/reference/graphs/sage/graphs/digraph_generators.html?highlight=circulant#sage.graphs.digraph_generators.DiGraphGenerators.Circulant
- https://doc.sagemath.org/html/en/reference/graphs/sage/graphs/graph_generators.html?highlight=circulant#sage.graphs.graph_generators.GraphGenerators.CirculantGraph
- https://doc.sagemath.org/html/en/reference/graphs/sage/graphs/generators/families.html?highlight=circulant#sage.graphs.generators.families.CirculantGraph
