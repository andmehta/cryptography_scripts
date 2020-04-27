from phi import phi
from gcd import gcd
from minv import minv


# calculates e for key generation
def calc_e(phi_n):
    r = 2
    while True:
        if gcd(r, phi_n) == 1:
            break
        else:
            r += 1
    return r


def find_n(p, q):
    n = p * q
    return n


def test_find_n():
    p = 1009
    q = 503
    n = 507527

    assert n == find_n(p, q)


def test_phi():
    phi_n = 506016
    n = 507527
    assert phi_n == phi(n)


def test_e():
    e = 5
    phi_n = 506016
    assert e == calc_e(phi_n)


def find_d(e, phi_n):
    d = minv(e, phi_n)
    return d


def test_find_d():
    d = 404813
    e = 5
    phi_n = 506016
    assert d == find_d(e, phi_n)

    d = 309962945807727846107
    e = 3
    phi_n = 464944418711591769160
    assert d == find_d(e, phi_n)


def find_C(P, e, n, phi_n):
    PP = P % n
    ee = e % phi_n
    C = pow(PP, ee, n)
    return C


def test_find_C():
    C = 32110
    e = 5
    n = 507527
    P = 423621
    phi_n = 506016
    assert C == find_C(P, e, n, phi_n)


def find_P(C, d, n):
    P = pow(C, d, n)
    return P


def test_find_P():
    P = 423621
    C = 32110
    d = 404813
    n = 507527

    assert P == find_P(C, d, n)


def signing_message(m, n, d):
    S = pow(m, d, n)
    return S


def test_signing_message():
    m = 14767019203392149587
    n = 507527
    d = 404813
    e = 3
    S = signing_message(m, n, d)

    mm = pow(S, e, n)
    assert m == mm


def RSA():
    # creating the keys
    p = int(input('Enter the p value:'))
    q = int(input('Enter the q value:'))
    n = p * q
    print('The value of n is: ', n)
    phi_n = (p - 1) * (q - 1)
    print('The value of phi is: ', phi_n)
    e = calc_e(phi_n)
    print('The value of e is: ', e)
    d = find_d(e, phi_n)
    print('The value of d is: ', d)

    # sending a message
    P = int(input('Enter the P value:'))
    PP = P % n
    ee = e % phi_n
    print('The value of PP is: ', PP)
    print('The value of ee is: ', ee)

    # encrypting the message using the message and public keys
    C = pow(PP, ee, n)  # P^Emod(n)

    # decrypting the message using the Crypted and private key
    print('The value of C is: ', C)
    P = pow(C, d, n)
    print('The value of P is: ', P)

    # signing with a hash
    m = int(input('Enter the m value:'))
    S = pow(m, d, n)
    print('The signature created is: ', S)

    # checking the hash signature
    print('Checking the signature using public keys.')
    mm = pow(S, e, n)
    if mm == m:
        print('Signature is correct. M calculated to be: ', mm)
    else:
        print('Incorrect Signature. M calculated to be: ', mm)
