compounds, capacity = map(int, input().split())
items = []
for _ in range(compounds):
    items.append(tuple(map(int, input().split())))

# Add value-to-weight ratio
items = [(cost, weight, cost / weight) for (cost, weight) in items]
# Sort by value-to-weight descending
items.sort(key=lambda x: x[2], reverse=True)

value = 0.0
weight = 0

for cost, wt, ratio in items:
    if weight + wt <= capacity:
        value += cost
        weight += wt
    else:
        remaining = capacity - weight
        value += ratio * remaining
        break

print(f"{value:.4f}")