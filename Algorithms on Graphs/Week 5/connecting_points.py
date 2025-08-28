# Uses python3
import sys
import math
import heapq

def minimum_distance(x, y):
    n = len(x)
    visited = [False] * n
    min_edge = [float('inf')] * n
    min_edge[0] = 0
    total_weight = 0.0

    # Priority queue: (cost, vertex)
    heap = [(0, 0)]

    while heap:
        cost, u = heapq.heappop(heap)

        if visited[u]:
            continue

        visited[u] = True
        total_weight += cost

        for v in range(n):
            if not visited[v]:
                dist = math.hypot(x[u] - x[v], y[u] - y[v])
                if dist < min_edge[v]:
                    min_edge[v] = dist
                    heapq.heappush(heap, (dist, v))

    return total_weight


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
