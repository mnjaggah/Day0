#this function determines whether a number is prime or not
#one can run a list comprehension to get the list of prime numbers
def is_prime(x):
    #define the unique conditions i.e 2 is prime
    if x < 2:
        return False
    elif x == 2:
        return x
    else:
        while x > 2:
            for n in range(2, x): #for loop to evaluate as prime
                if x % n == 0:
                    return False
                    break
            else:
                return x

#function returning a list comprehension to list prime no. in range            
def prime_range(m,n):
    return [x for x in range(m, n) if is_prime(x)]
