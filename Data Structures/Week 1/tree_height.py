# python3

import sys
import threading
from collections import defaultdict, deque


def compute_height(n, parents):
    # Replace this code with a faster implementation
    # max_height = 0
    # for vertex in range(n):
    #     height = 0
    #     current = vertex
    #     while current != -1:
    #         height += 1
    #         current = parents[current]
    #     max_height = max(max_height, height)
    # return max_height

    # Step 1: Build the tree
    tree = defaultdict(list)
    root = -1
    for child in range(n):
        parent = parents[child]
        if parent == -1:
            root = child
        else:
            tree[parent].append(child)

    # Step 2: BFS traversal to compute height
    height = 0
    queue = deque()
    queue.append((root, 1))  # (node, current depth)

    while queue:
        node, depth = queue.popleft()
        height = max(height, depth)
        for child in tree[node]:
            queue.append((child, depth + 1))

    return height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
