def fibonacci(n):
    if n <= 1:
        return n
    
    second_last = 0
    last_num = 1

    for _ in range(2, n+1):
        second_last, last_num = last_num, second_last + last_num

    return last_num

print(fibonacci(int(input())))