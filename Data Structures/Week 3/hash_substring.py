# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def poly_hash(s, prime, multiplier):
    hash_val = 0
    for c in reversed(s):
        hash_val = (hash_val * multiplier + ord(c)) % prime
    return hash_val

def precompute_hashes(text, pattern_len, prime, multiplier):
    n = len(text)
    hashes = [0] * (n - pattern_len + 1)
    last_substring = text[-pattern_len:]
    hashes[-1] = poly_hash(last_substring, prime, multiplier)
    y = 1
    for _ in range(pattern_len):
        y = (y * multiplier) % prime
    for i in reversed(range(n - pattern_len)):
        pre_hash = (
            multiplier * hashes[i + 1]
            + ord(text[i])
            - y * ord(text[i + pattern_len])
        ) % prime
        # Fix negative hash (Python `%` handles negatives differently)
        hashes[i] = (pre_hash + prime) % prime
    return hashes

def get_occurrences(pattern, text):
    result = []
    p_len = len(pattern)
    t_len = len(text)
    if p_len > t_len:
        return result

    prime = 1000000007
    multiplier = 263
    pattern_hash = poly_hash(pattern, prime, multiplier)
    hashes = precompute_hashes(text, p_len, prime, multiplier)

    for i in range(len(hashes)):
        if hashes[i] == pattern_hash and text[i:i + p_len] == pattern:
            result.append(i)

    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
