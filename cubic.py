from math import cos, sin, pi
from cmath import sqrt


def round_complex(c: complex) -> complex:
    """
    rounds the real and imaginary part of a complex number

    :param c: complex number
    :return : complex number with rounded real and imaginary part
    """

    c_real = round(c.real, 2)
    c_imag = round(c.imag, 2)

    return complex(c_real, c_imag)


def calculate_u_v(p: complex, q: complex) -> tuple:
    """
    calulates u and v
    """

    det = round_complex(sqrt((q / 2) ** 2 + (p / 3) ** 3))

    return (
        round_complex((-(q / 2) + det) ** (1 / 3)),
        round_complex((-(q / 2) - det) ** (1 / 3)),
    )


def zeta(k: int, n: int) -> complex:
    """
    calulates the unit roots
    """

    return complex(round(cos((2 * pi * k) / n), 2), round(sin((2 * pi * k) / n), 2))


def solve_cubic(p: complex, q: complex) -> list:
    """
    solves a cubiv equation in the p q form
    """
    u, v = calculate_u_v(p, q)

    x1 = round_complex(u + v)
    x2 = round_complex(u * zeta(1, 3)) + round_complex(v * zeta(2, 3))
    x3 = round_complex(u * zeta(2, 3)) + round_complex(v * zeta(1, 3))

    return [x1, x2, x3]


def main():
    # x^3-6x+20i
    p = -6
    q = 20j
    print(solve_cubic(p, q))


if __name__ == "__main__":
    main()
