# python3
import sys

def build_suffix_array(text):
    return sorted(range(len(text)), key=lambda i: text[i:])

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))
