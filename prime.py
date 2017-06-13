__author__ = "Mr Bancroft"

def filterOut(L1,L2):
    for i in L1:
        if i in L2:
            L2.remove(i)

def isPrime(n):
    i = 2
    if n <= 1:
        return False
    SqrtOfN = n**0.5
    while i <= SqrtOfN:
        if n % i == 0:
            return False
        i += 1
    else:
        return true

def primeGenerator(n):
    primes = [2,3,5,7,11]
    if n in xrange(1,len(primes)+1):
        return primes[:n]
    else:
        banlist = []
        count = 6
        while count <= n:
            Next = (primes[-2] + primes[-1] - primes[3])
            if not isPrime(Next):
                count -= 1
                banlist.append(Next)
            count += 1
            primes.append(Next)
        filterout(banlist,primes)
        return primes


