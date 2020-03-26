def minv(a, m):
    mo = m
    a = a % m
    prevx, x = 1, 0;
    prevy, y = 0, 1
    while m:
        q = int(a / m)
        x, prevx = prevx - q * x, x
        y, prevy = prevy - q * y, y
        a, m = m, a % m
    if a != 1:
        return 0
    else:
        return prevx % mo


def ecadd(p, a, x1, y1, x2, y2):
    print("ecadd(", p, ",", a, ",", x1, ",", y1, ",", x2, ",", y2, ")")
    if x2 != x1:
        s = ((y2 - y1) * minv((x2 - x1), p)) % p
    elif (x2 == x1) and (y2 == y1):
        s = ((3 * x1 * x1 + a) * minv(2 * y1, p)) % p
    else:
        return -1, -1
    x3 = (s * s - x1 - x2) % p
    y3 = (s * (x1 - x3) - y1) % p
    return x3, y3


def new_simple(numa, numb, numn):
    print(numa, "x=", numb, "(mod", numn, ")")
    nummin = minv(numa, numn)
    print("minv(", numa, ",", numn, ")=", nummin)
    print(numa, " * ", nummin, " * x = ")
    numa = numa * nummin
    print(numb, " * ", nummin, " (mod ", numn, ")")
    numb = numb * nummin
    print(numb, "(mod ", numn, ")=")
    nump = numb % numn
    print("x=", nump, "(mod", numn, ")")
