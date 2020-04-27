# returns the modulus inverse
def minv(a, m):
    mo = m
    a = a % m
    prevx, x = 1, 0
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