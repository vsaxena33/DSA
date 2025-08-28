#Uses python3

def reach(adj, x, y):
    #write your code here
    visited = [False] * len(adj)

    def dfs(v):
        visited[v] = True
        for neighbor in adj[v]:
            if not visited[neighbor]:
                dfs(neighbor)
    
    dfs(x)
    return 1 if visited[y] else 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    print(reach(adj, x, y))
