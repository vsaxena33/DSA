# python3
import sys
sys.setrecursionlimit(10000)

class Edge:
    __slots__ = ("start", "end", "child")
    def __init__(self, start, end, child):
        self.start = start      # inclusive
        self.end = end          # exclusive
        self.child = child      # Node

class Node:
    __slots__ = ("children",)
    def __init__(self):
        # map first character to Edge
        self.children = {}

def build_suffix_tree(text):
    """
    Build a compressed suffix tree by inserting each suffix using edge ranges
    and on-the-fly splitting. Return list of edge labels in any order.
    """
    n = len(text)
    root = Node()

    # Insert each suffix starting at sidx
    for sidx in range(n):
        cur = root
        i = sidx
        while True:
            c = text[i]
            edge = cur.children.get(c)
            if edge is None:
                # No edge with this starting char: create leaf edge to end
                cur.children[c] = Edge(i, n, Node())
                break

            # Walk along the existing edge as far as it matches
            e_start, e_end, child = edge.start, edge.end, edge.child
            k = 0
            # Compare text along the edge label with current suffix position
            while e_start + k < e_end and i + k < n and text[e_start + k] == text[i + k]:
                k += 1

            if e_start + k == e_end:
                # Consumed whole edge; descend to child
                cur = child
                i += k
                # If the suffix ends right here (shouldn’t happen before seeing '$'),
                # create an empty edge (not needed since text ends with '$'), so continue
                continue

            # Mismatch inside the edge: need to split
            mid = Node()

            # Replace the old edge with its prefix up to the split
            cur.children[c] = Edge(e_start, e_start + k, mid)

            # Old edge's remaining suffix becomes a child of the split node
            c_old = text[e_start + k]
            mid.children[c_old] = Edge(e_start + k, e_end, child)

            # New leaf from split node for the current suffix remainder
            c_new = text[i + k]
            mid.children[c_new] = Edge(i + k, n, Node())
            break

    # Collect all edge labels
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        for edge in node.children.values():
            result.append(text[edge.start:edge.end])
            stack.append(edge.child)
    return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))
