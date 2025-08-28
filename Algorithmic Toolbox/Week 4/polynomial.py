def karatsuba_poly(p, q):
    n = max(len(p), len(q))

    # Base case: if either polynomial is very small, use naive multiplication
    if n == 1:
        return [p[0] * q[0]]

    # Pad shorter list with zeros
    while len(p) < n:
        p.append(0)
    while len(q) < n:
        q.append(0)

    m = n // 2

    # Split polynomials into lower and higher parts
    p_low = p[:m]
    p_high = p[m:]
    q_low = q[:m]
    q_high = q[m:]

    # Recursive calls
    z0 = karatsuba_poly(p_low, q_low)
    z2 = karatsuba_poly(p_high, q_high)
    z1 = karatsuba_poly(
        [a + b for a, b in zip(p_low + [0] * (len(p_high) - len(p_low)), p_high)],
        [a + b for a, b in zip(q_low + [0] * (len(q_high) - len(q_low)), q_high)]
    )

    # z1 - z2 - z0
    z1 = [a - b - c for a, b, c in zip(z1 + [0] * (max(len(z2), len(z0)) - len(z1)),
                                      z2 + [0] * (max(len(z2), len(z0)) - len(z2)),
                                      z0 + [0] * (max(len(z2), len(z0)) - len(z0)))]

    # Assemble result
    result = [0] * (2 * n - 1)

    for i in range(len(z0)):
        result[i] += z0[i]
    for i in range(len(z1)):
        result[i + m] += z1[i]
    for i in range(len(z2)):
        result[i + 2 * m] += z2[i]

    # Remove trailing zeros (optional)
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return result

# Example usage
poly1 = [1, 2, 3, 4]  # 1x^3 + 2x^2 + 3x + 4
poly2 = [5, 6, 7, 8]  # 5x^3 + 6x^2 + 7x + 8
result = karatsuba_poly(poly1[::-1], poly2[::-1])  # Reverse: lowest degree first
print("Result (coefficients):", result[::-1])  # Reverse back for output
