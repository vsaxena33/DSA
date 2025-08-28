def merge_sort_and_count(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left_half, left_inv = merge_sort_and_count(arr[:mid])
    right_half, right_inv = merge_sort_and_count(arr[mid:])
    merged, split_inv = merge_and_count(left_half, right_half)

    # Total inversions = left + right + split
    total_inversions = left_inv + right_inv + split_inv
    return merged, total_inversions

def merge_and_count(left, right):
    i = j = 0
    merged = []
    inversions = 0

    # Merge step with inversion count
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += len(left) - i  # Count inversions here
            j += 1

    # Append remaining elements
    merged += left[i:]
    merged += right[j:]

    return merged, inversions

n = input()
arr = list(map(int, input().split()))
sorted_arr, inversion_count = merge_sort_and_count(arr)
print(inversion_count)