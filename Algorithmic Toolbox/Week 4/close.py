import math
import sys
sys.setrecursionlimit(1 << 25)

def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def closest_pair_rec(Px, Py):
    n = len(Px)
    if n <= 3:
        return min(distance(Px[i], Px[j]) for i in range(n) for j in range(i + 1, n))

    mid = n // 2
    midpoint = Px[mid][0]

    Qx = Px[:mid]
    Rx = Px[mid:]
    
    Qy = []
    Ry = []
    for point in Py:
        if point[0] <= midpoint:
            Qy.append(point)
        else:
            Ry.append(point)

    d1 = closest_pair_rec(Qx, Qy)
    d2 = closest_pair_rec(Rx, Ry)
    d = min(d1, d2)

    # Build the strip
    strip = [p for p in Py if abs(p[0] - midpoint) < d]

    # Check strip for closer pairs
    for i in range(len(strip)):
        for j in range(i+1, min(i + 8, len(strip))):
            d = min(d, distance(strip[i], strip[j]))
    return d

def closest_pair(points):
    Px = sorted(points, key=lambda p: p[0])  # sort by x
    Py = sorted(points, key=lambda p: p[1])  # sort by y
    return closest_pair_rec(Px, Py)

# Input
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Output
print(f"{closest_pair(points):.4f}")