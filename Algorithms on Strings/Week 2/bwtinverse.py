# python3
import sys

def InverseBWT(bwt):
    n = len(bwt)

    # Step 1: Tag each char with occurrence number in last column
    count = {}
    last_column = []
    for ch in bwt:
        count[ch] = count.get(ch, 0) + 1
        last_column.append((ch, count[ch]))

    # Step 2: Build first column (sorted last column)
    first_column = sorted(last_column)

    # Step 3: First occurrence of each character in first column
    first_occurrence = {}
    for i, (ch, _) in enumerate(first_column):
        if ch not in first_occurrence:
            first_occurrence[ch] = i

    # Step 4: Start from the row in last_column that contains '$'
    index = bwt.index('$')  # directly find $ in last column

    # Step 5: LF-mapping loop
    text = []
    for _ in range(n):
        ch, occ = last_column[index]
        text.append(ch)
        index = first_occurrence[ch] + occ - 1

    return ''.join(text[::-1])  # reverse at end because we built it backwards

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
