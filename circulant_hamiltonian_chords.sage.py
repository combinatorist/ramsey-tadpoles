graphs.CirculantGraph(13,[1,4]).show()
target = graphs.CirculantGraph(13,[1,4])
pattern = graphs.Cycle(13)
pattern = graphs.CycleGraph(13)
pattern.is_subgraph(target)
pattern.subgraph_search(target)
target.subgraph_search(pattern)
help(target.subgraph_search(pattern))
result = target.subgraph_search(pattern)
help(result)
dir(result)
result.edges
result.edges()
results = target.subgraph_search_iterator(pattern)
result = results.next()
rsults
results
result = next(results)
result.edges
result
next(results)
results = target.subgraph_search_iterator(pattern)
def generated_chords(generator, nodes):
    double = nodes * 2
    modulus = len(nodes)
    return set((double[i+generator] - double[i]) % modulus for i in range(modulus))
def all_generated_chords(generator, node_lists):
    return set().union(generated_chords(node_list) for node_list in node_lists)
all_generated_chords(results)
all_generated_chords(4, results)
def all_generated_chords(generator, node_lists):
    return set().union(generated_chords(generator, node_list) for node_list in node_lists)
all_generated_chords(4, results)
def all_generated_chords(generator, node_lists):
    return set().union(*generated_chords(generator, node_list) for node_list in node_lists)
def all_generated_chords(generator, node_lists):
    return set().union(*(generated_chords(generator, node_list) for node_list in node_lists))
all_generated_chords(4, results)
target.subgraph_search_count(pattern)
def generated_chords(generator, nodes):
    double = nodes + nodes[:generator]
    modulus = len(nodes)
    return set((double[i+generator] - double[i]) % modulus for i in range(modulus))
def generated_chords(generator, nodes):
    double = nodes + nodes[:generator]
    modulus = len(nodes)
    return set((double[i+generator] - double[i]) % modulus for i in range(modulus))
IPython.terminal.shortcuts.open_input_in_editor.
IPython.terminal.shortcuts.open_input_in_editor
Sage.terminal.shortcuts.open_input_in_editor
sage.terminal.shortcuts.open_input_in_editor
def search_cycles(modulus, root_generator):
    powers = get_residues(root_generator, modulus)
    target = graphs.CirculantGraph(modulus, powers)
    pattern = graphs.CycleGraph(modulus)
    results = target.subgraph_search_iterator(pattern)
    return all_generated_chords(root_generator, results)
search_cycles(13,4)
def get_residues(generator, modulo):
        residues = [1, generator]
            residue = generator * generator % modulo
    while residue not in residues:
            residues.append(residue)
                residue = residue * generator % modulo
    return residues
%paste
%pastemode
%paste def get_residues(generator, modulo):
    residues = [1, generator]
    residue = generator * generator % modulo
    while residue not in residues:
            residues.append(residue)
                residue = residue * generator % modulo
    return residues
%edit
search_cycles(13,4)
def all_generated_chords(generator, node_lists, modulus=None):
    if not modulus:
        start = next(node_lists)
        modulus = len(start)
    return set().union(*(generated_chords(generator, node_list) for node_list in node_lists))
%edit prev
def all_generated_chords(generator, node_lists, modulus=None):
    if not modulus:
        start = next(node_lists)
        modulus = len(start)
        node_lists = itertools.chain([start], node_lists)
    chords = set()
    for node_list in node_lists:
        chords.union(generated_chords(generator, node_list))
        if len(chords) + 1 == modulus:
            break
    return chords
search_cycles(13,4)
import itertools
search_cycles(13,4)
def search_cycles(modulus, root_generator):
    powers = get_residues(root_generator, modulus)
    target = graphs.CirculantGraph(modulus, powers)
    pattern = graphs.CycleGraph(modulus)
    results = target.subgraph_search_iterator(pattern)
    return all_generated_chords(root_generator, results, modulus)
search_cycles(13,4)
def all_generated_chords(generator, node_lists, modulus=None):
    if not modulus:
        start = next(node_lists)
        modulus = len(start)
        node_lists = itertools.chain([start], node_lists)
    chords = set()
    for node_list in node_lists:
        chords.extend(generated_chords(generator, node_list))
        if len(chords) + 1 == modulus:
            break
    return chords
search_cycles(13,4)
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
def search_examples():
    modulus = 3
    while True:
        modulus += 1
        for root_generator in range(2, modulus - 1):
            result = search_cycles(modulus, root_generator)
            if len(result) == modulus - 1:
                print(f'm:{modulus}, r:{root_generator}: all found')
            else:
                print(f'm:{modulus}, r:{root_generator}: {modulus - 1 - len(result)} missing')
                print(result)
search_examples()
def search_examples():
    modulus = 3
    while True:
        modulus += 1
        for root_generator in range(2, modulus - 1):
            if not coprime(root_generator, modulus):
                continue
            result = search_cycles(modulus, root_generator)
            if len(result) == modulus - 1:
                print(f'm:{modulus}, r:{root_generator}: all found')
            else:
                print(f'm:{modulus}, r:{root_generator}: {modulus - 1 - len(result)} missing')
                print(result)
%edit
search_examples()
def coprime(k,l):
    return gcd(k,l) == 1
coprime(13,4)
coprime(15,5)
search_examples()
%store dir(search_examples) >test
%store search_examples()
%store search_examples() > ramsey-results.txt
def search_examples(fileprefix='~/ramsey-results.txt'):
  with open(fileprefix + now(), 'w') as f:
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
                f.write(result)
search_examples()
from datetime.datetime import now
from datetime import now
from datetime import datetime.now
from datetime import datetime
def search_examples(fileprefix='~/ramsey-results.txt'):
  with open(fileprefix + datetime.now(), 'w') as f:
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
                f.write(result)
search_examples()
def search_examples(fileprefix='~/ramsey-results.txt'):
  with open(fileprefix + str(datetime.now()), 'w') as f:
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
                f.write(result)
search_examples()
def search_examples(fileprefix='~/ramsey-results.txt'):
  with open(fileprefix + str(today()), 'w') as f:
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
                f.write(result)
from datetime import today
from datetime import date.today
from datetime import date
from date import today
def today = date.today
today = date.today
def search_examples(fileprefix='~/ramsey-results.txt'):
  with open(fileprefix + str(today()), 'w') as f:
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
                f.write(result)
search_examples()
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
                f.write(result)
search_examples()
now = datetime.now
search_examples()
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
                f.write(sorted(result))
search_examples()
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
search_examples()
%edit _
%edit
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
                q
%edit
search_examples()
%edit search_examples
search_examples()
%edit search_examples
%edit search_examples
search_examples()
%edit search_examples
search_examples()
%edit search_examples
search_examples()
%edit search_examples
search_examples()
%save circulant_hamiltonian_chords.sage.py
%save
%save * circulant_hamiltonian_chords.sage.py
%save history circulant_hamiltonian_chords.sage.py
%save circulant_hamiltonian_chords.sage.py history
%save circulant_hamiltonian_chords.sage.py %history
%history
%history -f circulant_hamiltonian_chords.sage.py
