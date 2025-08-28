import random

def partition3(arr, low, high):
    pivot_index = random.randint(low, high)
    pivot = arr[pivot_index]
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]

    lt = low     # arr[low..lt-1] < pivot
    gt = high    # arr[gt+1..high] > pivot
    i = low + 1  # arr[lt+1..i-1] == pivot

    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    return lt, gt  # Return boundaries of the == pivot section

def quicksort3(arr, low, high):
    if low >= high:
        return
    lt, gt = partition3(arr, low, high)
    quicksort3(arr, low, lt - 1)
    quicksort3(arr, gt + 1, high)

# Reading input
n = int(input())
array = list(map(int, input().split()))

quicksort3(array, 0, n - 1)

# Output the sorted array
print(*array)
