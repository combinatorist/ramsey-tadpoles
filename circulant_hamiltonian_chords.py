from sage.all import *
from itertools import chain
from datetime import datetime
now = datetime.now

def generated_chords(generator, nodes):
    double = nodes + nodes[:generator]
    modulus = len(nodes)
    return set((double[i+generator] - double[i]) % modulus for i in range(modulus))

def get_residues(generator, modulo):
    residues = [1, generator]
    residue = generator * generator % modulo
    while residue not in residues:
            residues.append(residue)
            residue = residue * generator % modulo
    return residues

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
        node_lists = chain([start], node_lists)
    chords = set()
    for node_list in node_lists:
        chords.update(generated_chords(generator, node_list))
        if len(chords) + 1 == modulus:
            break
    return chords

def coprime(k,l):
    return gcd(k,l) == 1

def possible_chords(modulus, root_generator):
    pass

def id_unused_vertices():
    pass

def search_hamiltonian_via_subtraction(modulus=13, root_generator=4):
    powers = get_residues(root_generator, modulus)
    # powers = [1,4] # minimal undirected example
    powers = [4,12] # minimal directed example
    print(powers)
    target = digraphs.Circulant(modulus, powers)
    target.delete_vertex(4)
    hamiltonian = target.hamiltonian_path(5,0)
    print(hamiltonian.all_paths(5,0)[0])
    P = hamiltonian.plot()
    # P.show()
    P.save_image('figure.png')
    return P

# Historical runs have been moved manually to /data/ramsey/python/circulant
def search_examples(fileprefix='ramsey-results.txt', search_function=search_cycles):
  with open(fileprefix + str(now()), 'w') as f:
    modulus = 5
    while True:
        # skip evens for now (very slow, predictable counterexamples)
        modulus += 2
        # skip root_generator=2 (trivial?)
        # skip second half of root_generators (symmetric?)
        for root_generator in range(3, modulus // 2 + 1):
            if not coprime(root_generator, modulus):
                continue
            result = search_function(modulus, root_generator)
            expected = set(range(1, modulus))
            f.write(f'm:{modulus}, r:{root_generator}: {len(expected) - len(result)} missing:')
            f.write(str(sorted(expected.difference(result))))
            f.write("\n")
            f.flush()


#search_examples()
#%edit search_examples
if __name__ == "__main__":
  search_hamiltonian_via_subtraction()
