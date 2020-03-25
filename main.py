
def show_menu():
    print("\"square\": to calculate a squared congruence")
    print("\"power\": to calculate a powered congruence")
    print("\"simple\": to calculate a simple linear congruence")
    print("\"menu\": to see all available options")
    print("\"end\": to close program\n")


# greatest common divisor
def gcd(a, n, b):
    x = 0
    for x in range(1, n):
        if a*x % n == b:
            print("gcd = ", x)
            return x


def main():
    print("welcome to the Modulus Calculator")

    # initialize option before using in while loop
    option = "placeholder"

    print("type \"menu\" to see all available options")
    while option != "end":
        option = input("\nWhat would you like to do?: ")

        if option == "menu":
            show_menu()

        if option == "simple":
            print("ax = b mod(n)")
            num = int(input("a = "))
            num2 = int(input("b = "))
            modvalue = int(input("n = "))

            # solutions = gcd(num, modvalue, num2)
            for x in range(1, modvalue):
                if num*x % modvalue == num2:
                    print("solution = ", x)

        if option == "square":
            print("x^2 = b mod(n)")
            num = int(input("b = "))
            modvalue = int(input("n = "))

            for x in range(1, modvalue):
                if x*x % modvalue == num:
                    print(x)

        if option == "power":
            print("x^e = b mod(n)")
            num = int(input("b = "))
            modvalue = int(input("n = "))
            exponent = int(input("e = "))

            for x in range(1, modvalue):
                if x**exponent % modvalue == num:
                    print(x)
                    
        if option == "show_square":
            print("x^2 = b mod(n)")
            num = int(input("b = "))
            modvalue = int(input("n = "))

            for x in range(1, modvalue):
                print(x, "*", x, "%", modvalue, "=", x*x % modvalue)
                if x*x % modvalue == num:
                    print("the answer includes", x)


if __name__ == "__main__":
    main()
