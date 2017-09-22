Further Ramsey Support
======================
Tim Perisho
11/28/14
(originally a power point)

## Goals
- Find tadpole subgraphs
-
- Visualize proof steps
- Allow for programmable, interactive visualization and experimentation

## Data Types
- Ramsey coloring class
  - Defining adjacency matrix (red, blue, gray: -1,1,0)
    - There should be a method to create this based on an adjacency list, with a flag for multigraphs.
    - There are several ways I could allow multigraphs in the adjacency matrix, but I needn’t and shouldn’t for Ramsey coloring.
  -  Optional red and blue adjacency lists
    - Created from adjacency matrix or updated when a new edge is colored.
  - Optional node meta-data, including degree (in each non/color)
    - Created from adjacency matrix or updated when a new edge is colored.
  - Optional special adjacency list of path components (in each color)
    - Created from adjacency lists and deg-2 nodes or updated when a new edge is colored.
  - Optional “to-do list” metadata to keep track of which of the optional objects need to be updated with which edge colorings.
  - Method to add all chords of a given length
  - Methods to keep track of symmetries (for as long as they last)
- I should create a path graph data type based off lists (starting with min node id)
  - To compare paths: count (list function) how many times the shorter path or its reversal occurs in the longer one.
- I should use the cycle data type, but perhaps I would need to add a comparison function so that it can compare from any starting point.

## Path/Cycle/Tadpole finding algorithm
- Compress paths method
  - Find all nodes with degree 2
    - Might as well call a function to store all the node degrees in case I want them later, or at least re-order the adjacency lists by node degree.
  - Then, for each deg-2 node, get its entire deg-2 path component.
  - Index and store this as a special adjacency between two non-deg-2 nodes.
  - This special adjacency list would (often) give me a multigraph.
    - I could switch nodes and edges to make a new special adjacency matrix, but I don’t see the advantage of a matrix over a list in this case.
  - Order the special adjacency list to make it efficient to explore it (how?).
  - Then, I could easily find paths, cycles, and tadpoles, based on cycles of the right size and their adjacent path of a minimum size.
    - I might as well record all cycles I find on my way to finding a tadpole.
    - Obviously, find the cycle of the right size and then check the adjacent path components for one or a series of them that is long enough.
  - Taking it to the next level, I would want to be able to update this summary graph directly when new edges are colored.

## Old Ideas
- Generate JSON-style path/cycle analysis
  - Create list of all nodes
    - From each node, list all adjacent
    - Iterate to given depth or to each endpoint/repeated point (i.e. cycle)
      - E.g.: {1 : {2 : {3, 4}, 3},  2: {3, 4}, 1} …
      - I should include cycle repeat points
      - Should I include tadpole repeat points?
      - Should I do something to mark, cycle/tadpole repeat points in this data type
      - Basically, I want this to make every option explicit, which might be useful for other goals, but an efficient search (graph search/traversal) would probably be faster and take a lot less memory.
- Another option would be to create a list of all paths/cycles explicitly.
  - Instead of creating a list of all paths and cycles I could store ones I’ve found (w/meta data that it’s incomplete)
  - I could also just look for all cycles, because that’s more interesting in general.
    - In fact, this probably makes the most sense, because, even after I find a cycle or tadpole, it would probably take just as much processing to find a tail extension from a list of paths as from scratch.
  - How will I keep track of what paths I’ve tried?
