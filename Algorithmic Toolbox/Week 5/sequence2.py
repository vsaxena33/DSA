def longest_common_subsequence_length(A, B):
    n = len(A)
    m = len(B)
    
    # Initialize the DP table with 0s
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[n][m]

n = input()
A = list(map(int, input().split()))
m = input()
B = list(map(int, input().split()))
# Compute and print LCS length
print(longest_common_subsequence_length(A, B))