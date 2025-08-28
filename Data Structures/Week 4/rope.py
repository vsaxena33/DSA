# python3

import sys

class Rope:
    def __init__(self, s):
        self.s = list(s)  # Use list for mutability

    def result(self):
        return ''.join(self.s)

    def process(self, i, j, k):
        # Step 1: Extract the substring [i..j]
        substring = self.s[i:j+1]

        # Step 2: Remove it from the original position
        del self.s[i:j+1]

        # Step 3: Insert the substring after k-th character (1-based)
        # Note: k is the index in the new string, so insertion is at index k
        self.s[k:k] = substring


# Input handling
rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    rope.process(i, j, k)
print(rope.result())
