from math import sqrt

n = int(input())
k = int((-1 + sqrt(8*n + 1))/2)
print(k)

arr = []
for i in range(1, k):
    arr.append(i)
arr.append(n - sum(arr))
print(*arr)