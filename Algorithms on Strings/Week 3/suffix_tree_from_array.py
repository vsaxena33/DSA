# python3
import sys
from collections import defaultdict

def suffix_array_to_suffix_tree(sa, lcp, text):
    """
    Build suffix tree of the string text given its suffix array suffix_array
    and LCP array lcp_array. Return the tree as a mapping from a node ID
    to the list of all outgoing edges of the corresponding node. The edges in the
    list must be sorted in the ascending order by the first character of the edge label.
    Each edge is (child_id, start, end).
    """
    n = len(text)
    tree = defaultdict(list)

    # Node properties
    parent = []
    depth  = []  # string depth (distance from root in characters)
    estart = []  # edge start (text index) for edge from parent to this node
    eend   = []  # edge end (exclusive) for edge from parent to this node

    def new_node(p, d, s, e):
        node_id = len(parent)
        parent.append(p)
        depth.append(d)
        estart.append(s)
        eend.append(e)
        return node_id

    root = new_node(-1, 0, -1, -1)

    # Stack keeps path of the previous suffix: list of node ids from root to leaf
    stack = [root]

    for i, suf_start in enumerate(sa):
        lcp_prev = 0 if i == 0 else lcp[i - 1]

        # Pop until we are at string depth <= lcp_prev
        last_popped = None
        while depth[stack[-1]] > lcp_prev:
            last_popped = stack.pop()

        # If we need to split an edge
        if depth[stack[-1]] < lcp_prev:
            u = stack[-1]      # parent
            v = last_popped    # child to split (first node with depth > lcp_prev popped last)
            # Split at offset k from u
            k = lcp_prev - depth[u]
            # v edge label is text[estart[v]:eend[v]]
            # Create middle node w for text[estart[v] : estart[v] + k]
            w = new_node(u, lcp_prev, estart[v], estart[v] + k)
            # Rewire u -> w (replace edge u->v with u->w)
            # Remove edge (u -> v)
            # Find and replace in adjacency
            for idx, (child, s, e) in enumerate(tree[u]):
                if child == v:
                    tree[u][idx] = (w, estart[w], eend[w])
                    break
            else:
                # If not found (first time), append
                tree[u].append((w, estart[w], eend[w]))

            # Set w -> v for the remainder of the old edge
            parent[v] = w
            estart[v] = estart[v] + k
            # depth[v] stays the same
            tree[w].append((v, estart[v], eend[v]))

            stack.append(w)

        # Now attach the new leaf to the current top
        u = stack[-1]
        s = suf_start + (lcp_prev)
        leaf = new_node(u, n - suf_start, s, n)
        tree[u].append((leaf, s, n))

        # Push leaf to stack to represent current path
        stack.append(leaf)

    # Ensure edges of each node are sorted by the first character of the label
    for u in list(tree.keys()):
        tree[u].sort(key=lambda edge: text[edge[1]] if edge[1] >= 0 else '$')

    return dict(tree)

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    sa = list(map(int, sys.stdin.readline().strip().split()))
    lcp = list(map(int, sys.stdin.readline().strip().split()))
    print(text)
    tree = suffix_array_to_suffix_tree(sa, lcp, text)

    stack = [(0, 0)]
    result_edges = []
    while len(stack) > 0:
        (node, edge_index) = stack[-1]
        stack.pop()
        if not node in tree:
            continue
        edges = tree[node]
        if edge_index + 1 < len(edges):
            stack.append((node, edge_index + 1))
        print("%d %d" % (edges[edge_index][1], edges[edge_index][2]))
        stack.append((edges[edge_index][0], 0))
