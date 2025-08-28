# python3
import sys

NA = -1

def char_to_index(c):
    # Map A,C,G,T -> 0,1,2,3
    return {'A': 0, 'C': 1, 'G': 2, 'T': 3}[c]

class Node:
    def __init__(self):
        self.next = [NA] * 4  # edges for A,C,G,T

def build_trie(patterns):
    nodes = [Node()]  # root at index 0
    for p in patterns:
        current = 0
        for ch in p:
            idx = char_to_index(ch)
            if nodes[current].next[idx] == NA:
                nodes[current].next[idx] = len(nodes)
                nodes.append(Node())
            current = nodes[current].next[idx]
    return nodes

def is_leaf(node):
    return all(x == NA for x in node.next)

def solve(text, n, patterns):
    result = []
    trie = build_trie(patterns)
    for i in range(len(text)):
        current = 0
        j = i
        while True:
            if is_leaf(trie[current]):
                result.append(i)
                break
            if j >= len(text):
                break
            c = text[j]
            j += 1
            idx = char_to_index(c)
            if trie[current].next[idx] == NA:
                break
            current = trie[current].next[idx]
    return result

text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for _ in range(n):
    patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')
