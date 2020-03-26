from random import randrange


# Prime checker for ridiculously large primes
def primeChecker(p):
    # choose a random number
    flag = False
    for x in range(100):
        a = randrange(p)
        test = pow(a, p, p)
        if test != a:
            flag = True

    if flag:
        return "p is NOT a prime number"
    else:
        return "there is a 1/2^100 likelihood that p is NOT a prime number"
