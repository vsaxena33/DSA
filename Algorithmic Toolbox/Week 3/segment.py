def cover_segments(segments):
    # Sort segments by their right endpoint
    segments.sort(key=lambda x: x[1])
    
    points = []
    while segments:
        # Choose the right endpoint of the first segment
        point = segments[0][1]
        points.append(point)
        
        # Remove all segments covered by this point
        segments = [s for s in segments if s[0] > point]

    return points

# Read input
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Get the list of points
points = cover_segments(segments)

# Print output
print(len(points))
print(' '.join(map(str, points)))