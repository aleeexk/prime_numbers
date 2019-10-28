from itertools import groupby


def eratosthenes(n):
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve


ofile = open('output.txt', 'w')
x = 10**7
listt = eratosthenes(x)
listt = list(set(listt))
listt.sort()
ofile.write('{}\n'.format(listt))
ofile.close()
