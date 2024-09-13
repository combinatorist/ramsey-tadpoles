### platforms for search
- https://github.com/ciaranm/glasgow-subgraph-solver
  - checks and finds n times too many mappings for the same cycle size n
- SAT solver (Sage)
  - use below strategy (and sort through redundant and non-connected answers)
- spark (sql/bigquery)
  - partition by and join total mods of half-sized subsets (same strategy as sql) 
- rust
  - keep no memory
- python
  - [x] simply cut out memory intensive pre-optimizations
  - [x] manually del old objects? (not sure this really helps when the loop drops context anyway)

# converting my requirements into CNF form:
1. all nodes must have exactly 2 edges
  1. list each pair (with all their exclusions)
    1. actually exclusions can be listed separately from inclusions
2. result must be connected
  1. don't see how this could be represented without listing the actual answers
  1. maybe to list the possible answers and then let the solver pick between them?

