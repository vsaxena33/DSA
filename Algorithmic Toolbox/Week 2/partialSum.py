def fibonacciSeries(n):
    series = [0, 1]

    if n <= 1:
        return series[:n + 1]

    for _ in range(2, n + 1):
        series.append((series[-2] + series[-1]) % 10)

    return series

def fibonacciSum(n):
    quotient = n // 60
    remainder = n % 60
    return 280 * quotient + sum(fibonacciSeries(remainder))

m, n = map(int, input().split())
print(fibonacciSum(n) - fibonacciSum(m - 1))