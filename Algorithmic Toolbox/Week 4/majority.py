from collections import Counter

n = int(input())
seq = list(map(int, input().split()))

count = Counter(seq)
majority_threshold = n // 2 + 1

# Check if any value appears more than n/2 times
print(1 if any(freq >= majority_threshold for freq in count.values()) else 0)