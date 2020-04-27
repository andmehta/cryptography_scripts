#Finds the gcd of 2 integers
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

