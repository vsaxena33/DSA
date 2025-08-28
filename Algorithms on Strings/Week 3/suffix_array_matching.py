# python3
import sys

def build_suffix_array(text):
    # Ensure sentinel for correct comparisons
    if not text or text[-1] != '$':
        text += '$'
    n = len(text)
    order = [0]*n
    clazz = [0]*n

    alphabet = ['$','A','C','G','T']
    rank = {c:i for i,c in enumerate(alphabet)}
    cnt = [0]*len(alphabet)
    for ch in text:
        cnt[rank[ch]] += 1
    for i in range(1, len(cnt)):
        cnt[i] += cnt[i-1]
    for i in range(n-1, -1, -1):
        c = rank[text[i]]
        cnt[c] -= 1
        order[cnt[c]] = i

    clazz[order[0]] = 0
    classes = 1
    for i in range(1, n):
        if text[order[i]] != text[order[i-1]]:
            classes += 1
        clazz[order[i]] = classes-1

    l = 1
    tmp_order = [0]*n
    tmp_class = [0]*n
    while l < n:
        for i in range(n):
            tmp_order[i] = (order[i] - l) % n

        cnt = [0]*classes
        for i in range(n):
            cnt[clazz[tmp_order[i]]] += 1
        for i in range(1, classes):
            cnt[i] += cnt[i-1]
        for i in range(n-1, -1, -1):
            c = clazz[tmp_order[i]]
            cnt[c] -= 1
            order[cnt[c]] = tmp_order[i]

        tmp_class[order[0]] = 0
        classes_new = 1
        for i in range(1, n):
            cur, prev = order[i], order[i-1]
            mid, mid_prev = (cur + l) % n, (prev + l) % n
            if clazz[cur] != clazz[prev] or clazz[mid] != clazz[mid_prev]:
                classes_new += 1
            tmp_class[cur] = classes_new - 1
        clazz, classes = tmp_class[:], classes_new
        l <<= 1
    return order, text

def cmp_prefix(text, pattern, suffix_start):
    # Compare pattern with text[suffix_start:]
    i = 0
    n = len(text)
    while i < len(pattern) and suffix_start + i < n:
        if pattern[i] != text[suffix_start + i]:
            return -1 if pattern[i] < text[suffix_start + i] else 1
        i += 1
    # If we matched all pattern chars -> equal (0)
    return 0 if i == len(pattern) else -1  # pattern longer than suffix => pattern > suffix? Actually suffix ended with '$', so pattern > suffix -> return 1, but we want monotonicity; treat as greater than suffix so cmp returns 1. However text has '$' so suffix not end before '$' unless suffix is '$'. If pattern extends beyond '$', next char is '$' < 'A', so previous loop would have caught mismatch. This line is safe.

def find_occurrences(text, patterns):
    occs = set()
    sa, t = build_suffix_array(text)

    n = len(t)
    # For each pattern, binary search range of suffixes that start with it
    for p in patterns:
        # left bound: first suffix >= p
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if cmp_prefix(t, p, sa[mid]) <= 0:
                hi = mid
            else:
                lo = mid + 1
        left = lo

        # right bound: first suffix > p (by considering p with last char bumped, or use custom compare)
        lo, hi = 0, n
        # We search first suffix whose prefix comparison says suffix prefix is greater than p
        while lo < hi:
            mid = (lo + hi) // 2
            c = cmp_prefix(t, p, sa[mid])
            if c < 0:
                hi = mid
            else:
                lo = mid + 1
        right = lo

        # Collect occurrences in [left, right)
        for i in range(left, right):
            pos = sa[i]
            if pos < len(text):  # ignore the added '$' position
                occs.add(pos)

    return occs

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    occs = find_occurrences(text, patterns)
    print(" ".join(map(str, occs)))
