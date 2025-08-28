# python3

import sys

MOD = 10**9 + 7
BASE = 257

def compute_hashes(s):
    n = len(s)
    h = [0] * (n + 1)
    pows = [1] * (n + 1)
    for i in range(n):
        h[i+1] = (h[i] * BASE + ord(s[i])) % MOD
        pows[i+1] = (pows[i] * BASE) % MOD
    return h, pows

def get_hash(h, pows, start, length):
    end = start + length
    return (h[end] - h[start] * pows[length]) % MOD

def solve(k, text, pattern):
    n, m = len(text), len(pattern)
    if m > n:
        return []

    h_text, pows_text = compute_hashes(text)
    h_pat, pows_pat = compute_hashes(pattern)

    def first_mismatch(i, start):
        low, high = 0, m - start
        while low < high:
            mid = (low + high) // 2
            h1 = get_hash(h_pat, pows_pat, start, mid + 1)
            h2 = get_hash(h_text, pows_text, i + start, mid + 1)
            if h1 == h2:
                low = mid + 1
            else:
                high = mid
        return start + low

    result = []
    for i in range(n - m + 1):
        mismatches = 0
        pos = 0
        while mismatches <= k and pos < m:
            mismatch_pos = first_mismatch(i, pos)
            if mismatch_pos == m:
                break
            mismatches += 1
            pos = mismatch_pos + 1
        if mismatches <= k:
            result.append(i)
    return result

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            k, t, p = line.strip().split()
            ans = solve(int(k), t, p)
            print(len(ans), *ans)
