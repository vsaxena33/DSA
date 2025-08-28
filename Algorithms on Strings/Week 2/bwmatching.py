# python3
import sys
from collections import defaultdict

def PreprocessBWT(bwt):
    starts = {}
    sorted_bwt = sorted(bwt)
    for i, ch in enumerate(sorted_bwt):
        if ch not in starts:
            starts[ch] = i

    occ_counts_before = defaultdict(lambda: [0] * (len(bwt) + 1))
    for i, ch in enumerate(bwt):
        for c in starts.keys():
            occ_counts_before[c][i + 1] = occ_counts_before[c][i]
        occ_counts_before[ch][i + 1] += 1

    return starts, occ_counts_before

def CountOccurrences(pattern, bwt, starts, occ_counts_before):
    top = 0
    bottom = len(bwt) - 1
    while top <= bottom and pattern:
        symbol = pattern[-1]
        pattern = pattern[:-1]
        if symbol in starts:
            top = starts[symbol] + occ_counts_before[symbol][top]
            bottom = starts[symbol] + occ_counts_before[symbol][bottom + 1] - 1
        else:
            return 0
    return bottom - top + 1

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    starts, occ_counts_before = PreprocessBWT(bwt)
    occurrence_counts = []
    for pattern in patterns:
        occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
    print(' '.join(map(str, occurrence_counts)))
