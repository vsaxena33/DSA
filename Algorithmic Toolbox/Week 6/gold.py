def max_gold(W, weights):
    dp = [0] * (W + 1)
    for weight in weights:
        for w in range(W, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + weight)
    return dp[W]

if __name__ == "__main__":
    W, n = map(int, input().split())
    weights = list(map(int, input().split()))
    print(max_gold(W, weights))
