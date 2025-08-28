# python3
import sys

def solve(p, q):
    # For lengths 1..len(p), find the first substring of p not present in q.
    n = len(p)
    m = len(q)
    for L in range(1, n + 1):
        # Build set of all substrings of q of length L
        subs_q = set(q[i:i+L] for i in range(0, m - L + 1))
        # Scan substrings of p of length L; return the first not in subs_q
        for i in range(0, n - L + 1):
            s = p[i:i+L]
            if s not in subs_q:
                return s
    # Theoretically should never reach here since strings differ.
    return p  # fallback

p = sys.stdin.readline().strip()
q = sys.stdin.readline().strip()

ans = solve(p, q)

sys.stdout.write(ans + '\n')
