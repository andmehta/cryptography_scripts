from minv import minv


def part_1(a, p, g):
    alpha = pow(g, a, p)
    return alpha


def test_part_1():
    assert 48 == part_1(43, 79, 7)


def part_2(g, k, p, big_P, alpha):
    mu = pow(g, k, p)
    ak = pow(alpha, k, p)
    big_C = big_P * ak % p
    return mu, big_C


def test_part_2():
    mu_test, big_C_test = part_2(7, 5, 79, 21, 48)
    assert mu_test == 59 and big_C_test == 28


def part_3_1(mu, a, g, k, alpha, p):
    # first find mu^a
    mua = pow(mu, a, p)
    gka = pow(g, k * a, p)
    if mua == gka:
        return mua


def test_part_3_1():
    assert 54 == part_3_1(59, 43, 7, 5, 48, 79)


def part_3_2(big_C, big_X, alpha, k, p):
    big_X_inv = minv(big_X, p)
    big_P = big_C * big_X_inv
    big_P = big_P % p
    return big_P


def test_part_3_2():
    assert 21 == part_3_2(28, 54, 48, 5, 79)


def part_5(g, k, a, m, p):
    r = pow(g, k, p)
    k_inv = minv(k, p - 1)
    ar = a * r
    S = (m - ar) * k_inv % (p - 1)
    return r, S


def test_part_5():
    a = 43
    g = 7
    k = 5
    big_P = 21
    p = 79
    m = 12

    r, S = part_5(g, k, a, m, p)
    assert r == 59 and S == 41


def part_6(alpha, r, S, g, m, p):
    alphar = pow(alpha, r, p)
    rs = pow(r, S, p)
    gm = pow(g, m, p)

    if gm == (alphar * rs % p):
        return gm


def test_part_6():
    alpha = 48
    g = 7
    p = 79
    m = 12
    S = 41
    r = 59

    assert 8 == part_6(alpha, r, S, g, m, p)


def test_full_program():
    # original inputs
    a = 43
    g = 7
    k = 5
    big_P = 21
    p = 79
    m = 12
    alpha = part_1(a, p, g)
    mu_test, big_C_test = part_2(g, k, p, big_P, alpha)
    big_X = part_3_1(mu_test, a, g, k, alpha, p)
    r, S = part_5(g, k, a, m, p)
    assert big_P == part_3_2(big_C_test, big_X, alpha, k, p) and r == 59 and S == 41


# question 1 using El Gamal authentication and encryption
def main():
    ## part 1
    a = int(input("what is the private key (a)? "))
    p = int(input("what is the p value? "))
    g = int(input("what is the g value? "))

    alpha = part_1(a, p, g)

    ##Show answer to part 1
    print("The public key (alpha) is g^a (mod p):", alpha)

    ## part 2
    second_secret = int(input("what is the second secret (P)? "))
    masking_value = int(input("What is the masking value (k)? "))

    mu, big_C = part_2(g, masking_value, p, second_secret, alpha)

    ##Show answer to part 2
    print("the two values to be sent are mu:", mu, "and C:", big_C)

    ## part 3
    print("Using mu", mu, "and C", big_C, "first user can decrypt to get P", second_secret)

    big_X = part_3_1(mu, a, g, masking_value, alpha, p)

    ## if second secret is the same as the return of the sent calculations, than person 1 successfully decrypted the message
    if second_secret == part_3_2(big_C, big_X, alpha, masking_value, p):
        print("Person 1 successfully decrypted to find P")
        print("X = mu^a = (g^k)^a = (g^a)^k = a^k (mod p)")
        print("P = CX^(-1) = C(a^k)^(-1) = Pa^k *(a^k)^(-1)")
    else:
        print("something went wrong and person 1 could NOT decrypt to find P")

    ## part 5
    hash_m = int(input("What is the hash (m)? "))
    print("using k =", masking_value, "Alice makes 2 values r and S to verify her signature for hash,", hash_m)
    r, S = part_5(g, masking_value, a, hash_m, p)
    print("r =", r, "\nS =", S)

    ## part 6
    print("person 2 uses the value r:", r, "S:", S, "g:", g, "alpha", alpha, "and m:", hash_m)
    print("a^r * r^S == g^m")
    print("g^m =", part_6(alpha, r, S, g, hash_m, p))


if __name__ == "__main__":
    main()
