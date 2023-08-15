from sage.all import *
graphs.CirculantGraph(13,[1,4]).show()
target = graphs.CirculantGraph(13,[1,4])
pattern = graphs.CycleGraph(13)
pattern.is_subgraph(target)
pattern.subgraph_search(target)
target.subgraph_search(pattern)
#help(target.subgraph_search(pattern))
result = target.subgraph_search(pattern)
#help(result)
dir(result)
result.edges
result.edges()
results = target.subgraph_search_iterator(pattern)
result = next(results)
results = target.subgraph_search_iterator(pattern)
def generated_chords(generator, nodes):
    double = nodes * 2
    modulus = len(nodes)
    return set((double[i+generator] - double[i]) % modulus for i in range(modulus))
target.subgraph_search_count(pattern)
def generated_chords(generator, nodes):
    double = nodes + nodes[:generator]
    modulus = len(nodes)
    return set((double[i+generator] - double[i]) % modulus for i in range(modulus))
def generated_chords(generator, nodes):
    double = nodes + nodes[:generator]
    modulus = len(nodes)
    return set((double[i+generator] - double[i]) % modulus for i in range(modulus))
#sage.terminal.shortcuts.open_input_in_editor
def get_residues(generator, modulo):
    residues = [1, generator]
    residue = generator * generator % modulo
    while residue not in residues:
            residues.append(residue)
            residue = residue * generator % modulo
    return residues
import itertools
def search_cycles(modulus, root_generator):
    powers = get_residues(root_generator, modulus)
    target = graphs.CirculantGraph(modulus, powers)
    pattern = graphs.CycleGraph(modulus)
    results = target.subgraph_search_iterator(pattern)
    return all_generated_chords(root_generator, results, modulus)
def all_generated_chords(generator, node_lists, modulus=None):
    if not modulus:
        start = next(node_lists)
        modulus = len(start)
        node_lists = itertools.chain([start], node_lists)
    chords = set()
    for node_list in node_lists:
        chords.update(generated_chords(generator, node_list))
        if len(chords) + 1 == modulus:
            break
    return chords
search_cycles(13,4)
search_cycles(13,4)
def coprime(k,l):
    return gcd(k,l) == 1
coprime(13,4)
coprime(15,5)
#%store search_examples() > ramsey-results.txt
from datetime import datetime
from datetime import date
now = datetime.now
#%edit
def search_examples(fileprefix='ramsey-results.txt'):
  with open(fileprefix + str(now()), 'w') as f:
    modulus = 3
    while True:
        modulus += 1
        for root_generator in range(2, modulus - 1):
            if not coprime(root_generator, modulus):
                continue
            result = search_cycles(modulus, root_generator)
            if len(result) == modulus - 1:
                f.write(f'm:{modulus}, r:{root_generator}: all found')
            else:
                f.write(f'm:{modulus}, r:{root_generator}: {modulus - 1 - len(result)} missing')
                f.write(str(sorted(result)))
            f.write("\n")
            f.flush()
search_examples()
#%edit search_examples
search_examples()
#%history -f circulant_hamiltonian_chords.sage.py
