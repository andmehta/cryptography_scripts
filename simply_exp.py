
def simplify_base(a,b,p):
    one = a % p
    print(a,"(mod ",p,") = ",one)
    print(one,"^",b," (mod ",p,")")
    phis = phi(p)
    print("phi(",p,") = ",phis)
    two = b % phis
    print(b," mod ",phis," = ", two)
    print(one,"^",two," (mod ",p,")")

def gcd(a, b): 
  
    if (a == 0): 
        return b 
    return gcd(b % a, a) 
  
# A simple method to evaluate 
# Euler Totient Function 
def phi(n): 
  
    result = 1
    for i in range(2, n): 
        if (gcd(i, n) == 1): 
            result+=1
    return result 