def knapsack(W, weights):
    n = len(weights)
    dp = [0] * (W + 1)

    for i in range(n):
        w = weights[i]
        # Traverse backwards to avoid reusing the same item
        for j in range(W, w - 1, -1):
            dp[j] = max(dp[j], dp[j - w] + w)

    return dp[W]

# Input reading
W, n = map(int, input().split())
weights = list(map(int, input().split()))

# Output the result
print(knapsack(W, weights))
