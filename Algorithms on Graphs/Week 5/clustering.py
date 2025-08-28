# Uses python3
import sys
import math

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root == v_root:
            return False
        if self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = v_root
        else:
            self.parent[v_root] = u_root
            if self.rank[u_root] == self.rank[v_root]:
                self.rank[u_root] += 1
        return True

def clustering(x, y, k):
    n = len(x)
    edges = []

    # Build all edges with Euclidean distance
    for i in range(n):
        for j in range(i + 1, n):
            dist = math.hypot(x[i] - x[j], y[i] - y[j])
            edges.append((dist, i, j))

    # Sort edges by increasing distance
    edges.sort()

    dsu = DisjointSet(n)
    num_clusters = n

    for dist, u, v in edges:
        if dsu.find(u) != dsu.find(v):
            if num_clusters == k:
                # This is the smallest edge that would reduce clusters from k to k - 1
                return dist
            dsu.union(u, v)
            num_clusters -= 1

    return 0.0  # Shouldn't reach here

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
