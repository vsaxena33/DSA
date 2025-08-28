def optimal_sequence(n):
    dp = [0] * (n + 1)      # dp[i] = min operations to reach i
    prev = [0] * (n + 1)    # prev[i] = previous number before i

    for i in range(2, n + 1):
        # Start with +1 operation from i - 1
        min_ops = dp[i - 1] + 1
        prev[i] = i - 1

        if i % 2 == 0:
            if dp[i // 2] + 1 < min_ops:
                min_ops = dp[i // 2] + 1
                prev[i] = i // 2

        if i % 3 == 0:
            if dp[i // 3] + 1 < min_ops:
                min_ops = dp[i // 3] + 1
                prev[i] = i // 3

        dp[i] = min_ops

    # Reconstruct path from n to 1
    sequence = []
    while n > 0:
        sequence.append(n)
        n = prev[n]

    return dp[sequence[0]], list(reversed(sequence))

n = int(input())
steps, sequence = optimal_sequence(n)
print(steps)
print(*sequence)
