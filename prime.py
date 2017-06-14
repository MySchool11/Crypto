__author__ = "Mr Bancroft"

# a simple function to find all the prime numbers in a given range (determined by the
# max_number_to_find_primes_to variable in main.py

def get_primes(n):
    numbers = set(range(n,1,-1))                                # "set()" declares an unordered collection with no duplicates. "range()" creates a range of numbers starting at the passed in value n and ending at the item at index 1, counting back 1 every step so if 10 were passed it would create 2,3,4,5,6,7,8,9,10
    primes = []                                                 # declares an array "primes"
    while numbers:                                              # while loop that works through the range "numbers"
        p = numbers.pop()                                       # creates a variable "p" and places the last value in "numbers" into is using "pop()"
        primes.append(p)                                        # adds (appends) "p" to the "primes" array
        numbers.difference_update(set(range(p * 2, n + 1, p)))  # uses "difference_update" to
    return primes
