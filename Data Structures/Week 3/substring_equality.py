# python3

import random

class Solver:
    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self._prime1 = 10**9 + 7
        self._prime2 = 10**9 + 9
        self._multiplier = random.randint(1, self._prime1 - 1)

        self._precompute_powers()
        self._hash1 = self._precompute_hashes(self._prime1)
        self._hash2 = self._precompute_hashes(self._prime2)

    def _precompute_powers(self):
        self._powers1 = [1] * (self.n + 1)
        self._powers2 = [1] * (self.n + 1)
        for i in range(1, self.n + 1):
            self._powers1[i] = (self._powers1[i - 1] * self._multiplier) % self._prime1
            self._powers2[i] = (self._powers2[i - 1] * self._multiplier) % self._prime2

    def _precompute_hashes(self, prime):
        h = [0] * (self.n + 1)
        for i in range(1, self.n + 1):
            h[i] = (self._multiplier * h[i - 1] + ord(self.s[i - 1])) % prime
        return h

    def _substring_hash(self, hash_arr, powers, prime, start, length):
        y = powers[length]
        hash_val = (hash_arr[start + length] - y * hash_arr[start]) % prime
        return hash_val if hash_val >= 0 else hash_val + prime

    def ask(self, a, b, l):
        h1_a = self._substring_hash(self._hash1, self._powers1, self._prime1, a, l)
        h1_b = self._substring_hash(self._hash1, self._powers1, self._prime1, b, l)
        if h1_a != h1_b:
            return False
        h2_a = self._substring_hash(self._hash2, self._powers2, self._prime2, a, l)
        h2_b = self._substring_hash(self._hash2, self._powers2, self._prime2, b, l)
        return h2_a == h2_b


if __name__ == "__main__":
    s = input().strip()
    q = int(input())
    solver = Solver(s)
    for _ in range(q):
        a, b, l = map(int, input().split())
        print("Yes" if solver.ask(a, b, l) else "No")
