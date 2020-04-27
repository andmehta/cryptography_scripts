from phi import phi
from gcd import gcd


def numbers_of_order_base():
    Q = int(input("Are there 2 factors or 3?"))
    if Q == 2:
        numbers_of_order_two()
    else:
        numbers_of_order_three()


def pretty_print(A, Anum, B, Bnum, C, Cnum, calc):
    if int(calc) == 1:
        print(A, "^", Anum, ", ", B, "^", Bnum, ", ", C, "^", Cnum, " = ", calc, "\tphi(", calc, ") = ", phi(calc),
              sep='')
    else:
        print(A, "^", Anum, ", ", B, "^", Bnum, ", ", C, "^", Cnum, " = ", calc, "\tphi(", calc, ") = ", phi(calc),
              " elements of order ", calc, sep='')


def numbers_of_order_three():
    # Taking in the provided factors
    A = int(input('First factor:'))
    B = int(input('Second factor:'))
    C = int(input('Third factor:'))
    ansList = []
    print("Number of divisors are 2 * 2 * 2 = 8")
    # Iterating through 2^3, which is 8, in binary for the factor exponents
    ansList.append((A ** 0 * B ** 0 * C ** 0))
    ansList.append((A ** 0 * B ** 0 * C ** 1))
    ansList.append((A ** 0 * B ** 1 * C ** 0))
    ansList.append((A ** 0 * B ** 1 * C ** 1))
    ansList.append((A ** 1 * B ** 0 * C ** 0))
    ansList.append((A ** 1 * B ** 0 * C ** 1))
    ansList.append((A ** 1 * B ** 1 * C ** 0))
    ansList.append((A ** 1 * B ** 1 * C ** 1))
    pretty_print(A, 0, B, 0, C, 0, (A ** 0 * B ** 0 * C ** 0))
    pretty_print(A, 0, B, 0, C, 1, (A ** 0 * B ** 0 * C ** 1))
    pretty_print(A, 0, B, 1, C, 0, (A ** 0 * B ** 1 * C ** 0))
    pretty_print(A, 0, B, 1, C, 1, (A ** 0 * B ** 1 * C ** 1))
    pretty_print(A, 1, B, 0, C, 0, (A ** 1 * B ** 0 * C ** 0))
    pretty_print(A, 1, B, 0, C, 1, (A ** 1 * B ** 0 * C ** 1))
    pretty_print(A, 1, B, 1, C, 0, (A ** 1 * B ** 1 * C ** 0))
    pretty_print(A, 1, B, 1, C, 1, (A ** 1 * B ** 1 * C ** 1))
    print("The possible orders are ", (A ** 0 * B ** 0 * C ** 0), ",", (A ** 0 * B ** 0 * C ** 1), ",",
          (A ** 0 * B ** 1 * C ** 0), ",", (A ** 0 * B ** 1 * C ** 1), ",", (A ** 1 * B ** 0 * C ** 0), ",",
          (A ** 1 * B ** 0 * C ** 1), ",", (A ** 1 * B ** 1 * C ** 0), ",", (A ** 1 * B ** 1 * C ** 1), sep='')

    # printing the outcome of each round of multiplication/exponenation as well as printing the final answer,
    # which is the max.

    print('The final answer is: ', max(ansList))


def pretty_print_two(A, Anum, B, Bnum, calc):
    if int(calc) == 1:
        print(A, "^", Anum, ", ", B, "^", Bnum, " = ", calc, "\tphi(", calc, ") = ", phi(calc), sep='')
    else:
        print(A, "^", Anum, ", ", B, "^", Bnum, " = ", calc, "\tphi(", calc, ") = ", phi(calc), "elements of order ",
              calc, sep='')


def numbers_of_order_two():
    #  This is how to do it assuming two factors.
    A = int(input('First factor:'))
    B = int(input('Second factor:'))
    print("Number of divisors are 2 * 2 = 4")
    ansList = []
    ansList.append((A ** 0 * B ** 0))
    ansList.append((A ** 0 * B ** 1))
    ansList.append((A ** 1 * B ** 0))
    ansList.append((A ** 1 * B ** 1))
    pretty_print_two(A, 0, B, 0, (A ** 0 * B ** 0))
    pretty_print_two(A, 0, B, 1, (A ** 0 * B ** 1))
    pretty_print_two(A, 1, B, 0, (A ** 1 * B ** 0))
    pretty_print_two(A, 1, B, 1, (A ** 1 * B ** 1))
    print("The possible orders are ", (A ** 0 * B ** 0), ",", (A ** 0 * B ** 1), ",", (A ** 1 * B ** 0), ",",
          (A ** 1 * B ** 1), sep='')

    print('The final answer is: ', max(ansList))
