# python3
from itertools import permutations

def read_input(filename):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip()]

def overlap(a, b):
    """Return length of longest suffix of 'a' matching prefix of 'b'."""
    max_len = min(len(a), len(b))
    for i in range(max_len, 0, -1):
        if a[-i:] == b[:i]:
            return i
    return 0

def shortest_superstring(reads):
    n = len(reads)
    # Precompute overlaps
    ov = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                ov[i][j] = overlap(reads[i], reads[j])
    # DP to find shortest superstring
    dp = [[0]*n for _ in range(1<<n)]
    parent = [[-1]*n for _ in range(1<<n)]
    for mask in range(1<<n):
        for last in range(n):
            if not (mask & (1<<last)):
                continue
            prev_mask = mask ^ (1<<last)
            if prev_mask == 0:
                continue
            for i in range(n):
                if prev_mask & (1<<i):
                    val = dp[prev_mask][i] + ov[i][last]
                    if val > dp[mask][last]:
                        dp[mask][last] = val
                        parent[mask][last] = i
    # Reconstruct superstring
    mask = (1<<n) - 1
    last = max(range(n), key=lambda i: dp[mask][i])
    seq = []
    while last != -1:
        seq.append(last)
        temp = parent[mask][last]
        mask ^= (1<<last)
        last = temp
    seq = seq[::-1]
    # Build string
    s = reads[seq[0]]
    for i in range(1, len(seq)):
        olen = overlap(s, reads[seq[i]])
        s += reads[seq[i]][olen:]
    return s

if __name__ == "__main__":
    reads = read_input("dataset.txt")  # Replace with your dataset filename
    genome = shortest_superstring(reads)
    print(genome)
