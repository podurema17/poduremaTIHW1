import os, tempfile
import task1 as t1

def _write_tmp(text: str) -> str:
    fd, path = tempfile.mkstemp(prefix="nfa_", suffix=".txt")
    os.close(fd)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")
    return path

def test_even_number_of_ones():
    data = """
    2
    2
    0
    0
    0 0 0
    0 1 1
    1 0 1
    1 1 0
    """
    path = _write_tmp(data)
    try:
        nfa = t1.createNfaByPath(path)
        assert t1.executeNfaByInput(nfa, "0")
        assert not t1.executeNfaByInput(nfa, "1")
        assert t1.executeNfaByInput(nfa, "11")
        assert t1.executeNfaByInput(nfa, "1010")
    finally:
        os.remove(path)

def test_ends_with_01():
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
    try:
        nfa = t1.createNfaByPath(path)
        cases = [
            ("", False),
            ("0", False),
            ("1", False),
            ("01", True),
            ("101", True),
            ("010", False),
        ]
        for s, expected in cases:
            assert t1.executeNfaByInput(nfa, s) is expected
    finally:
        os.remove(path)
