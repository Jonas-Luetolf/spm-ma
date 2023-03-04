import numpy as np


def solve_simplex(m):
    BV = [0] * int((m.shape[1] - 1) / 2)

    while min(m[-1, :]) < 0:
        x = np.where(m[-1, :] == min(m[-1, :]))[0][0]
        i = np.where(
            m[:-1, -1] / (m[:-1, x] + 0.1)
            == min(i for i in m[:-1, -1] / (m[:-1, x] + 0.1) if i > 0)
        )[0][0]

        m[i, :] = m[i, :] / m[i, x]
        BV[i] = x + 1

        for y in range(0, m.shape[0]):
            if y == i:
                continue
            m[y, :] = m[y, :] - m[y, x] * m[i, :]

    solutions = [0] * int((m.shape[1] - 1) / 2)
    for i, index in enumerate(BV):
        if index != 0:
            solutions[index - 1] = round(m[i, -1], 2)

    return solutions


results = solve_simplex(
    np.array(
        [
            [2, 1, 1, 1, 0, 0, 2],
            [1, 2, 3, 0, 1, 0, 4],
            [2, 2, 1, 0, 0, 1, 8],
            [-4, -1, -4, 0, 0, 0, 0],
        ],
        dtype=np.float128,
    )
)

for i, result in enumerate(results):
    print(f"{i+1}: {result}")
