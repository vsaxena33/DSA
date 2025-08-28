# python3
import sys

NA = -1

def char_to_index(c):
    return {'A': 0, 'C': 1, 'G': 2, 'T': 3}[c]

class Node:
    def __init__(self):
        self.next = [NA] * 4
        self.patternEnd = False  # marks end of a pattern

def build_trie(patterns):
    nodes = [Node()]
    for p in patterns:
        current = 0
        for ch in p:
            idx = char_to_index(ch)
            if nodes[current].next[idx] == NA:
                nodes[current].next[idx] = len(nodes)
                nodes.append(Node())
            current = nodes[current].next[idx]
        nodes[current].patternEnd = True
    return nodes

def is_leaf(node):
    return all(x == NA for x in node.next)

def solve(text, n, patterns):
    result = []
    trie = build_trie(patterns)
    for i in range(len(text)):
        current = 0
        j = i
        matched_here = False
        while True:
            if trie[current].patternEnd:
                matched_here = True
                break
            if is_leaf(trie[current]):
                matched_here = True
                break
            if j >= len(text):
                break
            idx = char_to_index(text[j]) if text[j] in 'ACGT' else None
            if idx is None or trie[current].next[idx] == NA:
                break
            current = trie[current].next[idx]
            j += 1
        if matched_here:
            result.append(i)
    return result

text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for _ in range(n):
    patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')
