# Elliptic Curve Solver


# inputs: x value, mod_value, a, b
def ellipticCurveSolver(x, mod_value, a, b, show):
    # first solve for Y (uppercase is important here)
    big_Y = x ** 3 + a * x + b
    if show:
        print("big_Y = x**3 + a*x + b\twhere x =", x)
        print("big_Y =", big_Y)
    # Raise big_Y to power (p-1)/2
    if show:
        print("Raise big_Y to power (p-1)/2\twhere p =", mod_value)
        print(mod_value, "^((", mod_value, "-1)/2) (mod ", mod_value, ") = ",
              pow(big_Y, (mod_value - 1) // 2, mod_value), sep='')
    if pow(big_Y, (mod_value - 1) // 2, mod_value) == 1:
        # There must be a square root in that modulus
        if show:
            print("since that value was 1, there MUST be a square root so now raise big_Y to (p+1)/4")
            print(big_Y, "^((", mod_value, "+1)/4) (mod ", mod_value, ") = ",
                  pow(big_Y, (mod_value + 1) // 4, mod_value), sep='')
        value = pow(big_Y, (mod_value + 1) // 4, mod_value)
        if show:
            print("value =", pow(big_Y, (mod_value + 1) // 4, mod_value))
            print("value2 is possible by subtracting", value, "from", mod_value)
            print("value2 =", mod_value - value)
        value2 = mod_value - value

        return value, value2

    else:
        return "there are no Y values because pow(big_Y, (mod_value - 1)//2, mod_value) did NOT equal 1"
