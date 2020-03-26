# cryptography_scripts

## menu 
you'll first be shown an input field, I recommend typing in `menu` to show the available options

### `simple` from assignment 1 
Calculates a simple linear congruence equation involving some modulus. can display all relevant information if you type simple show. __TODO__ does not currently work


### `prime check` from assignment 2 question #2
calculates if a ridiculously large prime is likely. 
There is no definitive test, but using this test of a^p (mod p) = a, you can definitively say if a number is NOT prime if a number raised to p then mod p `pow(a, p, p) != a` 
if this fails, then it will tell you that the number is not prime. if it MIGHT be prime, it'll give you the likelihood it is NOT prime. `1/2^100`

### `new_simple` from assignment 2 take 2 question #3
Used for cases when you have (like Assign 2.2 #3)
```
13x+5≡ 15  (mod 23)
```

### 'elliptic show' from assignment 2 take 2 question #1
shows the step by step of 
1. finding if a point exists on a given elliptic curve
2. outputting that (those) point

### TODO the rest of these
- Add way to solve Assignment questions
- Prime version of Assign 2 #1
- Add ecadd
- Fix Assign 2 #5 & add show
## Assignment 1 ##
- [ ] Question 4: 
    ```
    4x = 7 (mod 19) --> show_simple
    ```
    ```
    4x = 7 (mod 19) --> simple
    ```
- [ ] Question 5:
    ```
    x^2 = 7 (mod 19) --> show_square
    ```
## Assignment 2 ##
- [ ] Question 1
    ```

    ```
- [ ] Question 2
    ```
    Is 32634334347834983  prime? --> prime check
    ```
## Assignment 2.2 ##
- [ ] Question 1
    ```
        Is there a point on the elliptic curve... at x = # --> show elliptic
    ```
- [ ] Question 2
    ```
        Let the point with x=3 with the small value of y... --> ecadd
    ```
- [ ] Question 3
    ```
        Solve 13x+5≡ 15  (mod 23) --> new_simple
    ```
- [ ] Question 4
    ```
        Solve x^2 = 9 (mod 17) --> square show
    ```
- [ ] Question 5
    ```
        Solve x^13= 5(mod 1763) -->power show || power
    ```
- [ ] Question 6
    ```

    ```
