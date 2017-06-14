__author__ = "Mr Bufford, Mr Bancroft"

# asymmetrical encryption attempt - using prime modulus
# keys must be primes

import random
import prime

max_number_to_find_primes_to = 1000000                      # does what it says - sets the maximum number up to which primes will be sought

primes = []                                                 # declares an array called "primes"
primes = prime.get_primes(max_number_to_find_primes_to)     # populates the array "primes" using the get_prime method in prime.py

count = primes.__len__()                                    # declares a variable "count" and makes it equal to the number of items in the "primes" array

publickey = primes [random.randint(0,count - 1)]
print("public key: " + str(publickey) + " (always a prime number)")
basenumber = random.randint (0, count * 10)
print("base number: " + str(basenumber) + " (base number, can be anything)")
aliceKey = primes [random.randint(0,count - 1)]
print("Alice's key: " + str(aliceKey) + " (always a prime number)")
bobKey = primes [random.randint(0,count - 1)]
print("Bob's key: " + str(bobKey) + " (always a prime number)")
aliceSend1=(basenumber**aliceKey)%publickey
print ("Alice sends to Bob the base number to the power of  Alice's key modulo the public key: " + str(aliceSend1))
bobSend1=(basenumber**bobKey)%publickey
print ("Bob sends to Alice the base number to the power of Bob's key modulo the public key: " + str(bobSend1))
alicedecode = (bobSend1**aliceKey)%publickey
print("Alice's code: " + str(alicedecode) + " (the result of what Bob sent to the power of Alice's key modulo the public key)")
bobdecode = (aliceSend1**bobKey)%publickey
print ("Bob's code: " + str(bobdecode) + " (the result of what Alice sent to the power of Bob's key modulo the public key)")
