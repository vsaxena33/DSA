# python3
import sys

def BWT(text):
    rotations = [text[i:] + text[:i] for i in range(len(text))]
    rotations.sort()
    return ''.join(row[-1] for row in rotations)

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))
