class State:
    __slots__ = ("isEnd", "edgesBy")
    def __init__(self):
        self.isEnd = False
        self.edgesBy = {}

class NFA:
    def __init__(self, startStates1, endStates, n, m, edges):
        self.M = m
        self.startStates = list(startStates1)
        self.states = [State() for _ in range(n)]
        for st in endStates:
            self.states[st].isEnd = True
        for u, a, v in edges:
            self.states[u].edgesBy.setdefault(a, []).append(v)

    def executeInput(self, input_str):
        stack = [(s, 0) for s in self.startStates]
        n = len(input_str)
        while stack:
            s, pos = stack.pop()
            st = self.states[s]
            if pos == n:
                if st.isEnd:
                    return True
                continue
            ch = input_str[pos]
            if ch < '0' or ch > '9':
                raise ValueError("Input must be digits")
            sym = ord(ch) - ord('0')
            if not (0 <= sym < self.M):
                raise ValueError("Symbol out of alphabet")
            for t in st.edgesBy.get(sym, []):
                stack.append((t, pos + 1))
        return False

def readPosInt(line):
    num = int(line.strip())
    if num <= 0:
        raise ValueError("Integer is not positive")
    return num

def readNotNegInts(line):
    lst = [int(p) for p in line.strip().split() if p]
    if not all(x >= 0 for x in lst):
        raise ValueError("Negative integer given")
    return lst

def readInputFile(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f]
    if len(lines) < 4:
        raise ValueError("File must have at least 4 lines")
    N = readPosInt(lines[0]); M = readPosInt(lines[1])
    if M > 9: raise ValueError("M must be <= 9")
    startStates = readNotNegInts(lines[2])
    endStates = readNotNegInts(lines[3])
    edges = []
    for raw in lines[4:]:
        if not raw.strip(): continue
        lst = readNotNegInts(raw)
        if len(lst) != 3: raise ValueError("Edge must have 3 ints")
        u,a,v = lst
        edges.append((u,a,v))
    return NFA(startStates, endStates, N, M, edges)

def createNfaByPath(path):
    return readInputFile(path)

def executeNfaByInput(nfa, input_str):
    for ch in input_str:
        if ch < '0' or ch > '9':
            raise ValueError("Input must be digits")
    return nfa.executeInput(input_str)

def task1(args):
    if len(args) != 2:
        raise ValueError("Invalid args")
    return executeNfaByInput(createNfaByPath(args[0]), args[1])

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python task1_nfa.py <nfa_file> <input_string>")
        sys.exit(1)
    ok = task1([sys.argv[1], sys.argv[2]])
    print("ACCEPTED" if ok else "REJECTED")