def lcs3(A, B, C):
    n, m, l = len(A), len(B), len(C)
    # Initialize 3D dp array
    dp = [[[0]*(l+1) for _ in range(m+1)] for __ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(1, l+1):
                if A[i-1] == B[j-1] == C[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(
                        dp[i-1][j][k],
                        dp[i][j-1][k],
                        dp[i][j][k-1]
                    )

    return dp[n][m][l]

n = input()
A = list(map(int, input().split()))
m = input()
B = list(map(int, input().split()))
o = input()
C = list(map(int, input().split()))

print(lcs3(A, B, C))