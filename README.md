ramsey-tadpoles
==============

Python module to explore Ramsey numbers for Tadpole graphs.

## Testing
Run `python test.py`

## Usage
Use ramsey_tadpoles.proof to get summarized results. For example:
```
(meta3) [618] ramseytadpoles% ipython
Python 3.6.1 (default, Apr  4 2017, 09:40:21)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.0.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from ramsey_tadpoles import proof

In [2]: proof(2,2,9)
Out[2]: (True, True, True, "0 overlap contradict's, 2 undirected edge contradict's")
```

## Future Enhancements:
* Check for Pan graphs
* Nearest Ramsey Upper Bound Calculator
* Efficient {Red, Blue, Neither} graph coloring data structure
* Method to find tadpoles within a colored graph
