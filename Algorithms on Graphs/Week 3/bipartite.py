# Uses python3

import sys
from collections import deque

def bipartite(adj):
    n = len(adj)
    color = [-1] * n  # -1 means unvisited

    for start in range(n):
        if color[start] == -1:  # Start BFS for an unvisited component
            queue = deque()
            queue.append(start)
            color[start] = 0  # Assign the first color

            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]  # Assign opposite color
                        queue.append(v)
                    elif color[v] == color[u]:
                        return 0  # Same color on both ends => not bipartite
    return 1  # All components are bipartite

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
