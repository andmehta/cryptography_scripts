from ellipticCurve import ellipticCurveSolver
from primeChecker import primeChecker
from new_simple import *
from power import powerCongruence
from simply_exp import *
from numsix import *


def show_menu():
    print("\"simple\": to calculate a simple linear congruence of style ax = b mod(n)")
    print("\"power\": to calculate a powered congruence of style x^e = b mod(n)")
    print("\"elliptic\": to calculate an elliptic curve of style Y=y^2 = x^3 + ax + b (mod p)")
    print("\"prime check\": check if an extremely large integer is prime")
    print("\"new_simple\": problem like 13x+5= 15(mod 23)")
    print("\"simplify\": 'Simplify the following expressions")
    print("\"menu\": to see all available options")
    print("\"ecadd\": To calculate #P using the double-and-add algorithm")
    print("\"order_num\": Find the possible orders of number in Zp")
    print("\"end\": to close program\n")


def main():
    print("welcome to the Modulus Calculator")

    # initialize option before using in while loop
    option = "placeholder"

    print("type \"menu\" to see all available options")
    while option != "end":
        option = input("\nWhat would you like to do?: ")

        if option == "simplify":
            print("a^b (mod p)")
            a = int(input("a = "))
            b = int(input("b = "))
            p = int(input("p = "))
            simplify_base(a, b, p)

        if option == "simple":
            print("ax = b mod(n)")
            num = int(input("a = "))
            num2 = int(input("b = "))
            mod_value = int(input("n = "))

            #fixed to use minv
            mod_inv = minv(num, mod_value)
            print("First find the modulus inverse of a")
            print("modulus inverse of", num, "=", mod_inv)
            solution = num2*mod_inv % mod_value
            print("multiply the mod inverse on both sides")
            print(mod_inv, "*", num, " = ", mod_inv, "*", num2, " (mod ", mod_value, ")", sep='')
            print("therefore: ", num2*mod_inv, " (mod ", mod_value, ")", sep='')
            print("solution =", solution)


        if option == "order_num":
            numbers_of_order_base()

        if option == "power":
            print("x^e = b mod(n)")
            num = int(input("b = "))
            mod_value = int(input("n = "))
            exponent = int(input("e = "))
            powerCongruence(num, exponent, mod_value, False)

        if option == "power show":
            print("x^e = b mod(n)")
            num = int(input("b = "))
            mod_value = int(input("n = "))
            exponent = int(input("e = "))
            answer = powerCongruence(num, exponent, mod_value, True)
            print("x =", answer)

        if option == "ecadd":
            print("Y=y^2 = x^3 + ax + b  (mod p)")
            a = int(input("a = "))
            b = int(input("b = "))
            x = int(input("x = "))
            p = int(input("p = "))
            print("P = (x1, y1)")
            x1 = int(input("x1 = "))
            y1 = int(input("y1 = "))
            print("REMEMBER: If using double and add, type in the same point as (x1, y1)")
            print("P = (x2, y2)")
            x2 = int(input("x2 = "))
            y2 = int(input("y2 = "))
            print("Calculate #P using...")
            np = int(input("#P = "))
            for x in range(1, np):
                (x2, y2) = ecadd(p, a, x1, y1, x2, y2)
                print(x + 1, "P = (", x2, ",", y2, ")", sep='')

        if option == "elliptic":
            print("Y=y^2 = x^3 + ax + b (mod p)")
            x = int(input("x = "))
            mod_value = int(input("p = "))
            a = int(input("a = "))
            b = int(input("b = "))
            values = ellipticCurveSolver(x, mod_value, a, b, False)
            print("y values are", values)

        if option == "elliptic show":
            print("Y=y^2 = x^3 + ax + b (mod p)")
            x = int(input("x = "))
            mod_value = int(input("p = "))
            a = int(input("a = "))
            b = int(input("b = "))
            values = ellipticCurveSolver(x, mod_value, a, b, True)
            print("y values are", values)

        if option == "prime check":
            prime = int(input("prime = "))
            isPrime = primeChecker(prime)

            print(isPrime)
        if option == "menu":
            show_menu()
        if option == "new_simple":
            print("ax = b mod(n)")
            numa = int(input("a = "))
            numb = int(input("b = "))
            numn = int(input("n = "))
            new_simple(numa, numb, numn)


if __name__ == "__main__":
    main()
