# Uses python3

import sys

def dfs(adj, used, order, x):
    used[x] = True
    for neighbor in adj[x]:
        if not used[neighbor]:
            dfs(adj, used, order, neighbor)
    order.append(x)  # post-visit action: add to order

def toposort(adj):
    used = [False] * len(adj)
    order = []
    for v in range(len(adj)):
        if not used[v]:
            dfs(adj, used, order, v)
    order.reverse()  # reverse the post-order to get topological order
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')
