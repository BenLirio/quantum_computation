import numpy as np

c = complex
gates = np.array([
    [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ],
    [
        [0, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ],
    [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ],
    [
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 0]
    ],
])

x = np.array([
    [1],
    [-1],
    [1],
    [-1]
])

t = np.transpose
mul = np.matmul
eye = np.eye(4, dtype=int)

i = 0
for A in gates:
    i += 1
    print(f"Gate {i}:")
    print(mul(A, x))
    if (mul(t(A), A) != eye).any():
        print(A)
    print()
