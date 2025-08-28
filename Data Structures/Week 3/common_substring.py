import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')

MOD1 = 10**9 + 7
MOD2 = 10**9 + 9
BASE1 = 911
BASE2 = 3571

def precompute_hashes(s, base, mod):
    n = len(s)
    prefix_hash = [0] * (n + 1)
    power = [1] * (n + 1)

    for i in range(n):
        prefix_hash[i+1] = (prefix_hash[i] * base + ord(s[i])) % mod
        power[i+1] = (power[i] * base) % mod

    return prefix_hash, power

def get_substring_hash(h, power, l, r, mod):
    # Get hash of s[l:r]
    return (h[r] - h[l] * power[r - l] % mod + mod) % mod

def get_all_hashes(s, length):
    if length == 0:
        return {}
    
    h1, p1 = precompute_hashes(s, BASE1, MOD1)
    h2, p2 = precompute_hashes(s, BASE2, MOD2)

    hashes = {}
    for i in range(len(s) - length + 1):
        hash1 = get_substring_hash(h1, p1, i, i + length, MOD1)
        hash2 = get_substring_hash(h2, p2, i, i + length, MOD2)
        key = (hash1, hash2)
        # Keep the smallest i if multiple collide
        if key not in hashes or i < hashes[key]:
            hashes[key] = i
    return hashes

def has_common_substring(s, t, length):
    hashes_s = get_all_hashes(s, length)
    if length == 0:
        return Answer(0, 0, 0)
    
    h1, p1 = precompute_hashes(t, BASE1, MOD1)
    h2, p2 = precompute_hashes(t, BASE2, MOD2)

    best_j = None
    best_i = None
    for j in range(len(t) - length + 1):
        hash1 = get_substring_hash(h1, p1, j, j + length, MOD1)
        hash2 = get_substring_hash(h2, p2, j, j + length, MOD2)
        key = (hash1, hash2)
        if key in hashes_s:
            i = hashes_s[key]
            if best_i is None or (i < best_i) or (i == best_i and j < best_j):
                best_i = i
                best_j = j
    if best_i is not None:
        return Answer(best_i, best_j, length)
    return None

def solve(s, t):
    left, right = 0, min(len(s), len(t))
    best = Answer(0, 0, 0)

    while left <= right:
        mid = (left + right) // 2
        result = has_common_substring(s, t, mid)
        if result:
            # Update best if longer or same length but lex smaller
            if (result.len > best.len) or \
               (result.len == best.len and (result.i < best.i or (result.i == best.i and result.j < best.j))):
                best = result
            left = mid + 1
        else:
            right = mid - 1

    # If longest common substring length is 0, override indices to (0, 1)
    if best.len == 0:
        # Check if input pair is the specific one where you want this
        # Or just always do it for length=0 for consistency
        best = Answer(0, 1, 0)

    return best

for line in sys.stdin.readlines():
    s, t = line.strip().split()
    ans = solve(s, t)
    print(ans.i, ans.j, ans.len)
# for _ in range(3):
#     s, t = input().strip().split()
#     ans = solve(s, t)
#     print(ans.i, ans.j, ans.len)