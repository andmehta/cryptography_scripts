# cryptography_scripts

## menu 
you'll first be shown an input field, I recommend typing in `menu` to show the available options

### `power` from assignment 2 take 2 question #5 Solves x^13= 5(mod 1763) or Solve x^2 = 9 (mod 17)
utilizes multiplicative inverse as well as phi to break down a complicated power congruence in the form of x^e = b (mod n)

### `prime check` from assignment 2 question #2 `Is 32634334347834983  prime?`
calculates if a ridiculously large prime is likely. 
There is no definitive test, but using this test of a^p (mod p) = a, you can definitively say if a number is NOT prime if a number raised to p then mod p `pow(a, p, p) != a` 
if this fails, then it will tell you that the number is not prime. if it MIGHT be prime, it'll give you the likelihood it is NOT prime. `1/2^100`

### `new_simple` from assignment 2 take 2 question #3
Used for cases when you have (like Assign 2.2 #3)
```
13x+5≡ 15  (mod 23)
```
### `simplify` from assignment 2 question #2 `123^456 = mod n`
Simplify the following expressions (do not solve, just simplify the base and exponent)
### `elliptic show` from assignment 2 take 2 question #1
shows the step by step of 
1. finding if a point exists on a given elliptic curve
2. outputting that (those) point

### `order_num` from Assignment 2 take 2 question #6
1.  Finds the possible orders of number in Zp

### `ecadd` from Assignment 2 take 2 question #2 solves Let the point with x=3 with the small value of y...
1. uses ECC and point addition to solve for a point on the elliptic curve
