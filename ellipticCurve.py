# Elliptic Curve Solver


# inputs: x value, mod_value, a, b
def ellipticCurveSolver(x, mod_value, a, b):
    # first solve for Y (uppercase is important here)
    big_Y = x**3 + a*x + b

    # Raise big_Y to power (p-1)/2
    if pow(big_Y, (mod_value - 1)//2, mod_value) == 1:
        # There must be a square root in that modulus
        value = pow(big_Y, (mod_value + 1)//4, mod_value)
        value2 = mod_value - value

        return value, value2

    else:
        return -1, -1
