#Uses python3

import sys
import heapq

def distance(adj, cost, s, t):
    n = len(adj)
    dist = [float('inf')] * n
    dist[s] = 0
    visited = [False] * n
    min_heap = [(0, s)]  # (distance, vertex)

    while min_heap:
        curr_dist, u = heapq.heappop(min_heap)

        if visited[u]:
            continue
        visited[u] = True

        for i in range(len(adj[u])):
            v = adj[u][i]
            weight = cost[u][i]
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(min_heap, (dist[v], v))

    return dist[t] if dist[t] != float('inf') else -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
