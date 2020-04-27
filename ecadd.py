from minv import minv


def ecadd(p, a, x1, y1, x2, y2):
    print("ecadd(", p, ",", a, ",", x1, ",", y1, ",", x2, ",", y2, ")", sep='')
    if x2 != x1:
        s = ((y2 - y1) * minv((x2 - x1), p)) % p
    elif (x2 == x1) and (y2 == y1):
        s = ((3 * x1 * x1 + a) * minv(2 * y1, p)) % p
    else:
        return -1, -1
    x3 = (s * s - x1 - x2) % p
    y3 = (s * (x1 - x3) - y1) % p
    return x3, y3
