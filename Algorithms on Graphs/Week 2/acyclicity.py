# Uses python3
import sys

def acyclic(adj):
    n = len(adj)
    visited = [False] * n
    rec_stack = [False] * n  # recursion stack

    def dfs(v):
        visited[v] = True
        rec_stack[v] = True
        for neighbor in adj[v]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif rec_stack[neighbor]:
                return True
        rec_stack[v] = False
        return False

    for node in range(n):
        if not visited[node]:
            if dfs(node):
                return 1  # cycle found
    return 0  # no cycle

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
