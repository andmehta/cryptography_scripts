
# Returns the GCD of a and b 
def gcd(a, b): 
  
    if (a == 0): 
        return b 
    return gcd(b % a, a) 
  
#finds phi 
def phi(n): 
  
    result = 1
    for i in range(2, n): 
        if (gcd(i, n) == 1): 
            result+=1
    return result 

#returns the modinv
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
    
#calculates e for key generation
def calc_e(phi_n):
    r = 2
    while True:
        if gcd(r, phi_n) == 1:
            break
        else:
            r += 1
    return r



#creating the keys
p = int(input('Enter the p value:'))
q = int(input('Enter the q value:'))
n = p * q
print('The value of n is: ', n)
phi_n = (p-1)*(q-1)
print('The value of phi is: ', phi_n)
e = calc_e(phi_n)
print('The value of e is: ', e)
d = minv(e,phi_n)
print('The value of d is: ', d)

#sending a message 
P = int(input('Enter the P value:'))
PP = P%n
ee = e%phi_n
print('The value of PP is: ', PP)
print('The value of ee is: ', ee)
#encrypting the message using the message and public keys
C = pow(PP,ee,n)#P^Emod(n)
#decrypting the message using the Crypted and private key
print('The value of C is: ', C)
P = pow(C,d,n)
print('The value of P is: ', P)
#signing with a hash
m = int(input('Enter the m value:'))
S = pow(m,d,n)
print('The signature created is: ', S)
#checking the hash signature
print('Checking the signature using public keys.')
mm = pow(S,e,n)
if mm == m:
    print('Signature is correct. M calculated to be: ', mm)
else:
    print('Incorrect Signature. M calculated to be: ',mm)