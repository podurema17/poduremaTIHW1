from dfa_utils import DFA, minimize_dfa, equivalent_dfa, is_universal
from collections import defaultdict

def dfa_from_edges(start, accepts, edges, alphabet=None):
    states = set()
    trans = defaultdict(dict)
    for (u, a), v in edges.items():
        states.add(u); states.add(v)
        trans[u][a] = v
    if alphabet is None:
        alphabet = {a for (_, a) in edges}
    return DFA(states, alphabet, start, set(accepts), trans)

def test_minimize_simple():
    edges = {(0,'a'):1, (1,'a'):0}
    dfa = dfa_from_edges(0, {0}, edges, {'a'})
    m = minimize_dfa(dfa)
    assert len(m.states) == 2
    assert equivalent_dfa(dfa, m)

def test_equivalence_diff():
    d1 = dfa_from_edges(0, {1}, {(0,'a'):1,(0,'b'):0,(1,'a'):1,(1,'b'):0}, {'a','b'})
    d2 = dfa_from_edges(0, {1}, {(0,'a'):0,(0,'b'):1,(1,'a'):0,(1,'b'):1}, {'a','b'})
    assert not equivalent_dfa(d1, d2)

def test_universal():
    edges = {(0,'a'):0,(0,'b'):0}
    dfa = dfa_from_edges(0, {0}, edges, {'a','b'})
    assert is_universal(dfa)
