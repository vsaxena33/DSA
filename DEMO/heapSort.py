def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # See if left child is larger
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if right child is larger
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Heapify the affected sub-tree

def heap_sort(arr):
    n = len(arr)
    
    # Build max heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

    return arr

# Example
arr = [7, 2, 9, 4, 1]
n = len(arr)
sorted_arr = heap_sort(arr.copy())
print("Sorted:", sorted_arr)
