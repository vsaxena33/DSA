def fibonacciRepitation(m):
    series = [0, 1]

    while True:
        series.append((series[-2] + series[-1]) % m)
        if series[-2] == 0 and series[-1] == 1:
            break

    return len(series[:-2])

def fibonacci(n):
    if n <= 1:
        return n
    
    second_last = 0
    last_num = 1

    for _ in range(2, n+1):
        second_last, last_num = last_num, (second_last + last_num) % 10

    return last_num

n, m = map(int, input().split())
repitation = fibonacciRepitation(m)
remainder = n % repitation
print(fibonacci(remainder))