# Uses python3

import sys
from collections import deque

def distance(adj, s, t):
    dist = [-1] * len(adj)
    dist[s] = 0
    q = deque()
    q.append(s)
    
    while q:
        current = q.popleft()
        for neighbor in adj[current]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[current] + 1
                q.append(neighbor)
                if neighbor == t:
                    return dist[neighbor]
    return dist[t]

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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
