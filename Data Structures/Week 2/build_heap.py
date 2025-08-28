# python3

def heapify(data, n, i, swaps):
    """Ensure the subtree rooted at index `i` follows the heap property."""
    smallest = i  # Start with the root node as the smallest.
    left = 2 * i + 1  # Left child index.
    right = 2 * i + 2  # Right child index.
    
    # Check if left child exists and is smaller than root.
    if left < n and data[left] < data[smallest]:
        smallest = left
    
    # Check if right child exists and is smaller than the smallest.
    if right < n and data[right] < data[smallest]:
        smallest = right
    
    # If the smallest is not the root, swap them and heapify the affected subtree.
    if smallest != i:
        data[i], data[smallest] = data[smallest], data[i]
        swaps.append((i, smallest))  # Record the swap.
        heapify(data, n, smallest, swaps)  # Heapify the subtree rooted at smallest.

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    n = len(data)
    # Start heapifying from the last non-leaf node and go upwards.
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, swaps)
    
    return swaps

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
