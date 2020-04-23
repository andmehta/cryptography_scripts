#Diffie Hellman Key Exchange

def part_1(p, g, a):
    alpha = pow(g, a, p)
    return alpha

def test_part_1():
    p = 107
    g = 2
    a = 40
    assert 41 == part_1(p, g, a)

def part_2(p, g, b):
    beta = pow(g, b, p)
    return beta
    
def test_part_2():
    p = 107
    g = 2
    b = 27
    assert 31 == part_2(p, g, b)

def part_3(p, beta, alpha, a, b):
    aliceKey = pow(beta, a, p)
    bobKey = pow(alpha, b, p)

    return aliceKey, bobKey
    
def test_part_3():
    p = 107
    a = 40
    b = 27
    alpha = 41
    beta = 31

    aKey, bKey = part_3(p, beta, alpha, a, b)
    assert aKey == bKey and aKey == 83

    

def main():
    print("Diffie Hellman Key exchange")

    #part 1
    p = int(input("p = "))
    g = int(input("g = "))
    secret_a = int(input("What is Alice's secret? "))
    alpha = part_1(p, g, secret_a)
    print("Alice's public key is", alpha, "\n")

    #part 2
    secret_b = int(input("What is Bob's secret? "))
    beta = part_2(p, g, secret_b)

    print("Bob's public key is", beta, "\n")

    #part_3
    print("Alice and Bob determine the common secret by finding K")
    print("Alice does beta^a and Bob does alpha^b")
    print("These will be the same")
    aKey, bKey = part_3(p, beta, alpha, secret_a, secret_b)
    print("Kab = beta^a = alpha^b =", aKey, "=", bKey)
    print("the public key is", aKey)
    

if __name__ == "__main__":
    main()
