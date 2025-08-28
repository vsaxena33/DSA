n, m = map(int, input().split())
segs = []
for _ in range(n):
    l, r = map(int, input().split())
    segs.append((l, r))

points = list(map(int, input().split()))

# Events: (coordinate, type, index)
# type: 'L' for left, 'R' for right, 'P' for point
events = []

for l, r in segs:
    events.append((l, 'L'))
    events.append((r, 'R'))

for i, p in enumerate(points):
    events.append((p, 'P', i))  # Include original index to restore order later

# Sort events: by coordinate, then 'L' < 'P' < 'R' to ensure proper counting
events.sort(key=lambda x: (x[0], x[1]))

# Sweep line
count = 0
result = [0] * m

for event in events:
    if event[1] == 'L':
        count += 1
    elif event[1] == 'R':
        count -= 1
    else:  # event[1] == 'P'
        _, _, idx = event
        result[idx] = count

print(*result)