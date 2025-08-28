# Uses python3

import sys

def negative_cycle(adj, cost):
    n = len(adj)
    # Initialize distances to all nodes as infinite
    dist = [0] * n

    # Run Bellman-Ford algorithm for n times
    for i in range(n):
        updated = False
        for u in range(n):
            for idx, v in enumerate(adj[u]):
                weight = cost[u][idx]
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    updated = True
        # If in the nth iteration we can still update, then there's a negative cycle
        if i == n - 1 and updated:
            return 1  # Negative cycle detected

    return 0  # No negative cycle found

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
