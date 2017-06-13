__author__ = "Mr Bancroft"

# a simple function to find all the prime numbers in a given range (determined by the
# max_number_to_find_primes_to variable in main.py

def get_primes(n):
    numbers = set(range(n,1,-1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p * 2, n + 1, p)))
    return primes
