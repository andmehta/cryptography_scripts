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


### TODO the rest of these
- Add way to solve Assignment questions
## Assignment 1 ##
- [ ] Question 4: 
    ```
    show_simple
    ```
    ```
    simple
    ```
- [ ] Question 5:
    ```
    show_square
    ```
## Assignment 2 ##
