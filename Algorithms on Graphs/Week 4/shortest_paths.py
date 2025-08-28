# Uses python3

import sys
import queue

def shortet_paths(adj, cost, s, distance, reachable, shortest):
    n = len(adj)
    distance[s] = 0
    reachable[s] = 1
    
    # Bellman-Ford algorithm
    for i in range(n - 1):
        for u in range(n):
            for idx, v in enumerate(adj[u]):
                if distance[u] != 10**19 and distance[v] > distance[u] + cost[u][idx]:
                    distance[v] = distance[u] + cost[u][idx]
                    reachable[v] = 1
    
    # Detect vertices affected by negative cycles
    affected = [0] * n
    for u in range(n):
        for idx, v in enumerate(adj[u]):
            if distance[u] != 10**19 and distance[v] > distance[u] + cost[u][idx]:
                affected[v] = 1

    # BFS to mark all nodes reachable from any node in a negative cycle
    q = queue.Queue()
    for i in range(n):
        if affected[i]:
            q.put(i)

    while not q.empty():
        u = q.get()
        shortest[u] = 0
        for v in adj[u]:
            if shortest[v]:
                q.put(v)
                shortest[v] = 0

    # Mark reachable nodes
    for i in range(n):
        if distance[i] != 10**19:
            reachable[i] = 1


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
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])
