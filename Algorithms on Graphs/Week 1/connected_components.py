# Uses python3

def dfs(adj, visited, node):
    visited[node] = True
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(adj, visited, neighbor)

def number_of_components(adj):
    visited = [False] * len(adj)
    result = 0
    for v in range(len(adj)):
        if not visited[v]:
            dfs(adj, visited, v)
            result += 1
    return result

if __name__ == '__main__':
    # Read n and m
    n, m = map(int, input().split())
    
    # Read m edges
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    
    print(number_of_components(adj))
