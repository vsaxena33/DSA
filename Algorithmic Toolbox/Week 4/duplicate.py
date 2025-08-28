def binary_search_first_occurrence(arr, low, high, key):
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            result = mid
            high = mid - 1  # continue searching on the left side
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return result

n = int(input())
seq = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))

result = [binary_search_first_occurrence(seq, 0, n - 1, x) for x in arr]

print(*result)