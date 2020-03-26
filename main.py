from ellipticCurve import ellipticCurveSolver
from primeChecker import primeChecker
from new_simple import *


def show_menu():
    print("\"simple\": to calculate a simple linear congruence of style ax = b mod(n)")
    print("\"square\": to calculate a squared congruence of style x^2 = b mod(n)")
    print("\"square show\": show how to calculate a squared congruence")
    print("\"power\": to calculate a powered congruence of style x^e = b mod(n)")
    print("\"elliptic\": to calculate an elliptic curve of style Y=y^2 = x^3 + ax + b (mod p)")
    print("\"prime check\": check if an extremely large integer is prime")
    print("\"new_simple\": problem like 13x+5= 15(mod 23)")
    print("\"menu\": to see all available options")
    print("\"end\": to close program\n")


# greatest common divisor
def gcd(a, n, b):
    x = 0
    for x in range(1, n):
        if a * x % n == b:
            print("gcd = ", x)
            return x


def main():
    print("welcome to the Modulus Calculator")

    # initialize option before using in while loop
    option = "placeholder"

    print("type \"menu\" to see all available options")
    while option != "end":
        option = input("\nWhat would you like to do?: ")

        if option == "simple":
            print("ax = b mod(n)")
            num = int(input("a = "))
            num2 = int(input("b = "))
            mod_value = int(input("n = "))

            # solutions = gcd(num, mod_value, num2)
            for x in range(1, mod_value):
                if num * x % mod_value == num2:
                    print("solution = ", x)

        if option == "square":
            print("x^2 = b mod(n)")
            num = int(input("b = "))
            mod_value = int(input("n = "))

            for x in range(1, mod_value):
                if x * x % mod_value == num:
                    print(x)

        if option == "square show":
            print("x^2 = b mod(n)")
            num = int(input("b = "))
            mod_value = int(input("n = "))

            for x in range(1, mod_value):
                print(x, "*", x, "%", mod_value, "=", x * x % mod_value)
                if x * x % mod_value == num:
                    print("the answer includes", x)

        if option == "power":
            print("x^e = b mod(n)")
            num = int(input("b = "))
            mod_value = int(input("n = "))
            exponent = int(input("e = "))

            for x in range(1, mod_value):
                if x ** exponent % mod_value == num:
                    print(x)

        if option == "elliptic":
            print("Y=y^2 = x^3 + ax + b (mod p)")
            x = int(input("x = "))
            mod_value = int(input("p = "))
            a = int(input("a = "))
            b = int(input("b = "))
            values = ellipticCurveSolver(x, mod_value, a, b)
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
            new_simple(numa,numb,numn)


if __name__ == "__main__":
    main()
