__author__ = "Mr Bufford"

# asymmetrical encryption attempt - using prime modulus
# keys must be primes

import random
import prime

primes = []
primes = prime.get_primes(1000000)
primes2 = primes
count = primes.__len__()
publickey = primes [random.randint(0,count - 1)]
print("publickey: " + str(publickey) + " (always a prime number)")
basenumber = random.randint (0, count * 10)
print("base number: " + str(basenumber) + " (base number, can be anything)")
aliceKey = primes [random.randint(0,count - 1)]
print("Alice's key: " + str(aliceKey) + " (always a prime number)")
bobKey = primes2 [random.randint(0,count - 1)]
print("Bob's key: " + str(bobKey) + " (always a prime number)")
aliceSend1=(basenumber**aliceKey)%publickey
print ("Alice sends to Bob the base number to the power of  Alice's key modulo the public key: " + str(aliceSend1))
bobSend1=(basenumber**bobKey)%publickey
print ("Bob sends to Alice the base number to the power of Bob's key modulo the public key: " + str(bobSend1))
alicedecode = (bobSend1**aliceKey)%publickey
print("Alice code: " + str(alicedecode) + " (the result of Bob send to the power of Alice's key modulo the public key)")
bobdecode = (aliceSend1**bobKey)%publickey
print ("Bob code: " + str(bobdecode) + " (the result of Alice send to the power of Bob's key modulo the public key)")
