def fibonacciSeries(n):
    series = [0, 1]

    if n <= 1:
        return series[:n + 1]

    for _ in range(2, n + 1):
        series.append((series[-2] + series[-1]) % 10)

    return series

n = int(input())
quotient = n // 60
remainder = n % 60
print((280 * quotient + sum(fibonacciSeries(remainder))) % 10)