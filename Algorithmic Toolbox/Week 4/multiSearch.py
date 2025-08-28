def binary_search(arr, low, high, key):
    if high < low:
        return -1  # Key not found

    mid = (low + high) // 2  # Calculate the midpoint

    # Check if the key is present at mid
    if arr[mid] == key:
        return mid
    # If the key is smaller than mid, search in the left subarray
    elif arr[mid] > key:
        return binary_search(arr, low, mid - 1, key)
    # If the key is larger than mid, search in the right subarray
    else:
        return binary_search(arr, mid + 1, high, key)

n = int(input())
seq = list(map(int, input().split()))
m = input()
arr = list(map(int, input().split()))

result = []
for i in arr:
    result.append(binary_search(seq, 0, n - 1, i))

print(*result)