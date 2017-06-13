__author__ = "Mr Bufford"

# asymmetrical encryption attempt - using prime modulus
# keys must be primes

import random
import prime

primes = []
primes = primeGenerator(1000)
primes2 = [2,3,5,7,11,13,15,17,19,23,27]
publickey = primes [random.randint(0,10)]
print("publickey: " + str(publickey))
basenumber = random.randint (0,100)
print("base number: " + str(basenumber))
aliceKey = primes [random.randint(0,10)]
print("Alice's key: " + str(aliceKey))
bobKey = primes2 [random.randint(0,10)]
print("Bob's key: " + str(bobKey))
aliceSend1=(basenumber**aliceKey)%publickey
print ("Alice send (basenumber ** alicekey) % publickey): " + str(aliceSend1))
bobSend1=(basenumber**bobKey)%publickey
print ("Bob send (basenumber ** bobkey) % publickey): " + str(bobSend1))
alicedecode = (bobSend1**aliceKey)%publickey
print("Alice code: " + str(alicedecode))bobdecode = (aliceSend1**bobKey)%publickey
print ("Bob code: " + str(bobdecode))
