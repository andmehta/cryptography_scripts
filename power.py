# finding a variable to a specific power using phi and multiplicative inverse for a congruence equation
from new_simple import minv
from phi import phi


def powerCongruence(b, power, mod_value, show):
    new_mod = phi(mod_value)
    if show:
        print("first phi() the mod value: phi(", mod_value, ") = ", phi(mod_value), sep='')

    # find multiplicative inverse
    multi_inv = minv(power, new_mod)
    if show:
        print("next find the multiplicative inverse:", multi_inv)

    # raise both sides to this multiplicative inverse
    if show:
        print("raise both sides to the multiplicative inverse: x^(", power, "*", multi_inv, ") = ", b, "^", multi_inv,
              " (mod ", mod_value, ")", sep='')
        print("recall x^y = x mod(n) IF y=1 mod phi(n)")
        print("As ", power, "*", multi_inv, " = 1 (mod ", new_mod, "), so too must x^(", power, "*", multi_inv,
              ") = x (mod ", mod_value, ")", sep='')
        print("Therefore x = ", b, "^", multi_inv, " (mod ", mod_value, ")", sep='')

    # solve using pow function
    answer = pow(b, multi_inv, mod_value)

    return answer
