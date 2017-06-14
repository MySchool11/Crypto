__author__ = "Mr Bufford, Mr Bancroft"

# asymmetrical encryption attempt - using prime modulus
# keys must be primes

import random
import prime

max_number_to_find_primes_to = 1000000                      # does what it says - sets the maximum number up to which primes will be sought

primes = []                                                 # declares an array called "primes"
primes = prime.get_primes(max_number_to_find_primes_to)     # populates the array "primes" using the get_prime method in prime.py

count = primes.__len__()                                    # declares a variable "count" and makes it equal to the number of items in the "primes" array

public_key = primes [random.randint(0,count - 1)]           # randomly picks a prime from the array "primes" and puts it in "public_key"
print("public key: " + str(public_key) + " (always a prime number)")
base_number = random.randint (0, count * 10)                # picks a random number between 0 and 10 * the number of primes in array "primes" and puts it in "base_number"
print("base number: " + str(base_number) + " (base number, can be anything)")
alice_key = primes [random.randint(0,count - 1)]            # randomly picks a prime from the array "primes" and puts it in "alice_key"
print("Alice's key: " + str(alice_key) + " (always a prime number)")
bob_key = primes [random.randint(0,count - 1)]              # randomly picks a prime from the array "primes" and puts it in "bob_key"
print("Bob's key: " + str(bob_key) + " (always a prime number)")
alice_send = (base_number**alice_key)%public_key            # calculates the number Alice will send and puts it in "alice_send"
print ("Alice sends to Bob the base number to the power of  Alice's key modulo the public key: " + str(alice_send))
bob_send = (base_number**bob_key)%public_key                # calculates the number Bob will send and puts it in "bob_send"
print ("Bob sends to Alice the base number to the power of Bob's key modulo the public key: " + str(bob_send))
alice_decode = (bob_send**alice_key)%public_key             # calculates the number Alice will end up with after checking the information passed from Bob and puts it in "alice_decode"
print("Alice's code: " + str(alice_decode) + " (the result of what Bob sent to the power of Alice's key modulo the public key)")
bob_decode = (alice_send**bob_key)%public_key               # calculates the number Bob will end up with after checking the information passed from Alice and puts it in "bob_decode"
print ("Bob's code: " + str(bob_decode) + " (the result of what Alice sent to the power of Bob's key modulo the public key)")
has_passed = alice_decode == bob_decode                     # calculate a boolean (true of false) which reflects whether Bob and Alice's decoded numbers are the same
print ("The key exchanged worked correctly: " + str(has_passed))
