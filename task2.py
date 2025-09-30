from collections import deque

class State:
    __slots__=("isEnd","edgesBy")
    def __init__(self):
        self.isEnd=False
        self.edgesBy={}

class NFA:
    def __init__(self,startStates,endStates,n,m,edges):
        self.M=m
        self.startStates=list(startStates)
        self.states=[State() for _ in range(n)]
        for e in endStates:
            self.states[e].isEnd=True
        for u,a,v in edges:
            self.states[u].edgesBy.setdefault(a,[]).append(v)

def readPosInt(line):
    num=int(line.strip())
    if num<=0: raise ValueError("Integer is not positive")
    return num

def readNotNegInts(line):
    lst=[int(p) for p in line.strip().split() if p]
    if not all(x>=0 for x in lst):
        raise ValueError("Negative integer given")
    return lst

def readInputFile(path):
    with open(path,"r",encoding="utf-8") as f:
        lines=[ln.rstrip("\n") for ln in f]
    if len(lines)<4: raise ValueError("File must have at least 4 lines")
    N=readPosInt(lines[0]); M=readPosInt(lines[1])
    if M>9: raise ValueError("M must be <= 9")
    startStates=readNotNegInts(lines[2]); endStates=readNotNegInts(lines[3])
    edges=[]
    for raw in lines[4:]:
        if not raw.strip(): continue
        lst=readNotNegInts(raw)
        if len(lst)!=3: raise ValueError("Edge must have 3 ints")
        u,a,v=lst
        edges.append((u,a,v))
    return NFA(startStates,endStates,N,M,edges)

class DFA:
    def __init__(self,nfa):
        self.M=nfa.M
        self.startState=set(sorted(nfa.startStates))
        self.states={}
        dq=deque([frozenset(self.startState)])
        while dq:
            cur=dq.popleft()
            if cur in self.states: continue
            mapping={}
            for i in cur:
                st=nfa.states[i]
                for sym,tgt_list in st.edgesBy.items():
                    mapping.setdefault(sym,set()).update(tgt_list)
            self.states[cur]=mapping
            for tgt in mapping.values():
                nxt=frozenset(tgt)
                if nxt not in self.states and nxt not in dq:
                    dq.append(nxt)
        self.endOneStates=set(i for i,st in enumerate(nfa.states) if st.isEnd)

    def executeInput(self,input_str):
        cur=frozenset(self.startState)
        for ch in input_str:
            if ch<'0' or ch>'9': raise ValueError("Symbol not in alphabet")
            sym=ord(ch)-48
            if not (0<=sym<self.M): raise ValueError("Symbol not in alphabet")
            mapping=self.states.get(cur)
            if not mapping: return False
            tgt=mapping.get(sym)
            if not tgt: return False
            cur=frozenset(tgt)
        return any(x in self.endOneStates for x in cur)

def createDfaByPath(path):
    return DFA(readInputFile(path))

def _state_sort_key(fs):
    return (len(fs), ",".join(str(x) for x in sorted(fs)))

def outputDfa(path,dfa):
    try: open(path,"x",encoding="utf-8").close()
    except FileExistsError: pass
    def write(txt,mode="a"):
        with open(path,mode,encoding="utf-8") as f: f.write(txt)
    write(f"{len(dfa.states)}\n",mode="w")
    write(f"{dfa.M}\n")
    write(f"{set(sorted(dfa.startState))}\n")
    accepting=[fs for fs in dfa.states if any(x in dfa.endOneStates for x in fs)]
    accepting.sort(key=_state_sort_key)
    for i,fs in enumerate(accepting):
        if i<len(accepting)-1: write(f"{set(sorted(fs))} ")
        else: write(f"{set(sorted(fs))} \n")
    for fs,trans in sorted(dfa.states.items(),key=lambda kv:_state_sort_key(kv[0])):
        for sym in sorted(trans.keys()):
            write(f"{set(sorted(fs))} {sym} {sorted(list(trans[sym]))}\n")

def task2(args):
    if len(args)!=2: raise ValueError("Invalid args")
    dfa=createDfaByPath(args[0]); outputDfa(args[1], dfa)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python task2_dfa.py <nfa_file> <dfa_out_file>")
        sys.exit(1)
    task2([sys.argv[1], sys.argv[2]])
    print(f"DFA written to {sys.argv[2]}")