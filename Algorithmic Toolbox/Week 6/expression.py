def eval_op(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

def get_maximum_value(expression):
    digits = list(map(int, expression[::2]))
    ops = list(expression[1::2])
    n = len(digits)
    
    min_dp = [[0]*n for _ in range(n)]
    max_dp = [[0]*n for _ in range(n)]
    
    for i in range(n):
        min_dp[i][i] = digits[i]
        max_dp[i][i] = digits[i]

    for s in range(1, n):  # s is the subexpression length
        for i in range(n - s):
            j = i + s
            min_val = float('inf')
            max_val = float('-inf')
            for k in range(i, j):
                op = ops[k]
                a = eval_op(max_dp[i][k], max_dp[k+1][j], op)
                b = eval_op(max_dp[i][k], min_dp[k+1][j], op)
                c = eval_op(min_dp[i][k], max_dp[k+1][j], op)
                d = eval_op(min_dp[i][k], min_dp[k+1][j], op)
                min_val = min(min_val, a, b, c, d)
                max_val = max(max_val, a, b, c, d)
            min_dp[i][j] = min_val
            max_dp[i][j] = max_val

    return max_dp[0][n-1]

if __name__ == "__main__":
    expr = input().strip()
    print(get_maximum_value(expr))
