import os, tempfile, random
import task1 as t1
import task2 as t2

def _write_tmp(text: str) -> str:
    fd, path = tempfile.mkstemp(prefix="nfa_", suffix=".txt")
    os.close(fd)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")
    return path

def test_dfa_equivalence_with_nfa():
    data = """
    3
    2
    0
    2
    0 0 0
    0 1 0
    0 0 1
    1 1 2
    """
    path = _write_tmp(data)
    out = path + ".dfa.txt"
    try:
        dfa = t2.createDfaByPath(path)
        nfa = t1.createNfaByPath(path)
        for _ in range(100):
            s = "".join(random.choice("01") for _ in range(random.randint(0, 6)))
            assert nfa.executeInput(s) == dfa.executeInput(s)
        t2.outputDfa(out, dfa)
        assert os.path.exists(out)
    finally:
        if os.path.exists(path): os.remove(path)
        if os.path.exists(out): os.remove(out)
