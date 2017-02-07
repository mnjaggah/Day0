def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        while x > 2:
            for n in range(2, x):
                if x % n == 0:
                    return False
                    break
            else:
                return True
            
