def knapsack(weights, values, capacity):
    n = len(weights)
    # Create DP table with (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom up manner
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                # Max of including or not including the item
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                # Cannot include the item
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]

# Example usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

max_value = knapsack(weights, values, capacity)
print("Maximum value in knapsack:", max_value)
