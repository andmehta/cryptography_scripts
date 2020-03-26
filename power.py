# finding a variable to a specific power using phi and multiplicative inverse for a congruence equation
from new_simple import minv


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


# A simple method to evaluate
# Euler Totient Function
def phi(n):
    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            result += 1
    return result


def powerCongruence(b, power, mod_value, show):
    new_mod = phi(mod_value)
    if show:
        print("first phi() the mod value: phi(", mod_value, ") =", phi(mod_value))

    # find multiplicative inverse
    multi_inv = minv(power, new_mod)
    if show:
        print("next find the multiplicative inverse:", multi_inv)

    # raise both sides to this multiplicative inverse
    if show:
        print("raise both sides to the multiplicative inverse: x^(", power, ")*", multi_inv, "=", b, "^", multi_inv,
              "(mod", mod_value, ")")
        print("recall x^y = x mod(n) IF y=1 mod phi(n)")
        print("As", power, "*", multi_inv, "= 1 mod(", new_mod, "), so too must x^(", power, "*", multi_inv,
              ") = x (mod", mod_value, ")")
        print("Therefore x =", b, "^", multi_inv, "(mod", mod_value, ")")

    # solve using pow function
    answer = pow(b, multi_inv, mod_value)

    return answer

