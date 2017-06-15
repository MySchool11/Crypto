__author__ = "Mr Bufford, Mr Bancroft"

# asymmetrical encryption attempt - using prime modulus
# keys must be primes

from random import randint                                  # imports the "randint" function from the "random" Python library
from prime import get_primes                                # imports the "get_primes" function from the "prime.py" file

# you can use import like this:
# import random
# but then each time you wish to use a function from random library you must declare "random.randint"
# declaring the functions you wish to use and the libraries from which they came makes the code much easier to understand
# also once declared instead of "random.randint(number, number)" for each usage you can just type "randint(number, number)", much easier and cleaner

max = 1000000                                               # "min" holds the minimum number the user can enter for the primes search
min = 10                                                    # "max" holds the maximum number the user can enter for the primes search

print("This program will show you how Diffie-Hellman key exchange works\n")
user_limit = input("Choose a limit for the prime search (" + str(min) +" - " + str(max) + "): ")

try:
    max_number_to_find_primes_to = int(user_limit)          # does what it says - sets the maximum number up to which primes will be sought using the user input
except:
    print("!! You entered something other than a number !! so using a random number between " + str(min) + " and " + str(max))
    max_number_to_find_primes_to = randint (min, max)       # pick a random number between min and max and put it in "max_number_to_find_primes_to"

if max_number_to_find_primes_to < min:                      # If statement to ensure the user input is not below the minimum and if it is, reset it to the minimum
    print("!! You entered a number less than the minimum !! so using " + str(min) + " instead")
    max_number_to_find_primes_to = min
if max_number_to_find_primes_to > max:                      # If statement to ensure the user input is not above the maximum and if it is, reset it to the maximum
    print("!! You entered a number above the maximum !! so using " + str(max) + " instead")
    max_number_to_find_primes_to = max

primes = get_primes(max_number_to_find_primes_to)           # declares an array called "primes" and populates it using the "get_prime) method in prime.py

count = primes.__len__()                                    # declares a variable "count" and makes it equal to the number of items in the "primes" array

public_key = primes [randint(0,count - 1)]                  # randomly picks a prime from the array "primes" and puts it in "public_key"
print("\npublic key (always a prime number): " + str(public_key) + "\n")
base_number = randint (0, count * 10)                       # picks a random number between 0 and 10 * the number of primes in array "primes" and puts it in "base_number"
print("base number (base number, can be anything): " + str(base_number) + "\n")
alice_key = primes [randint(0,count - 1)]                   # randomly picks a prime from the array "primes" and puts it in "alice_key"
print("Alice's key (always a prime number): " + str(alice_key))
bob_key = primes [randint(0,count - 1)]                     # randomly picks a prime from the array "primes" and puts it in "bob_key"
print("Bob's key (always a prime number): " + str(bob_key) + "\n")
alice_send = (base_number**alice_key)%public_key            # calculates the number Alice will send and puts it in "alice_send"
print ("Alice sends to Bob the base number to the power of  Alice's key modulo the public key: " + str(alice_send))
bob_send = (base_number**bob_key)%public_key                # calculates the number Bob will send and puts it in "bob_send"
print ("Bob sends to Alice the base number to the power of Bob's key modulo the public key: " + str(bob_send) + "\n")
alice_decode = (bob_send**alice_key)%public_key             # calculates the number Alice will end up with after checking the information passed from Bob and puts it in "alice_decode"
print("Alice's code (the result of what Bob sent to the power of Alice's key modulo the public key): " + str(alice_decode))
bob_decode = (alice_send**bob_key)%public_key               # calculates the number Bob will end up with after checking the information passed from Alice and puts it in "bob_decode"
print ("Bob's code (the result of what Alice sent to the power of Bob's key modulo the public key): " + str(bob_decode) + "\n")
has_passed = alice_decode == bob_decode                     # calculate a boolean (true of false) which reflects whether Bob and Alice's decoded numbers are the same
print ("The key exchanged worked correctly: " + str(has_passed))
exit_string = input("\nPress enter to exit.....")           # waits for the user to press enter to end the program