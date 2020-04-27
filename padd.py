#points on an elliptic curve

## given by slide 55 on Cryptography - 04
def isxoncurve(p,a,b,x): 
    t=(pow(x,3,p)+a*x + b)%p
    if pow(t, (p-1)/2, p)==1:
        y=pow(t, (p+1)/4,  p)
        return  y%p, -y%p   #(x,y) & (x,-y) on curve
    else:
        return  0,0 # no point on curve at x

## modinv given
def modinv(a, m):
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

def padd(p,x1,y1,x2,y2): #add P and Q where x1 ≠ x2
    y = y2-y1
    x = x2-x1
    minv = modinv(x,p)
    s=(y*minv) %p
    s2 = s*s
    x3=(s2-x1-x2) % p
    y3=(s*(x1-x3)-y1) % p
    return (x3,y3) #R=P+Q

def pdouble(p,a,x,y): #double P=(x,y)
	s=((3*x*x+a)*modinv(2*y,p)) %p	
	x3=(s*s-x-x) % p
	y3=(s*(x-x3)-y) % p
	return (x3,y3)#P+P


p = 37347466511
x1 = 1
y1 = 2
x2 = 6 
y2 = 8
print(padd(p,x1,y1,x2,y2))
print(pdouble(p, 1, x1, y1))
