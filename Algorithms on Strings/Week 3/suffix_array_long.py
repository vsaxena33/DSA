# python3
import sys

def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """
    # text is guaranteed to end with '$' per problem statement
    n = len(text)
    # Map characters to ranks; alphabet is '$', 'A', 'C', 'G', 'T'
    order = [0] * n
    clazz = [0] * n

    # Initial counting sort by single characters
    alphabet = ['$','A','C','G','T']
    cnt = [0] * len(alphabet)
    rank = {c:i for i,c in enumerate(alphabet)}

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
        clazz[order[i]] = classes - 1

    l = 1
    tmp_order = [0] * n
    tmp_class = [0] * n
    while l < n:
        # Sort by (clazz[i], clazz[(i + l) % n]) using counting sort by second then first
        for i in range(n):
            tmp_order[i] = (order[i] - l) % n

        # counting sort by first key = clazz[tmp_order[i]]
        cnt = [0] * classes
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

    return order

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))
