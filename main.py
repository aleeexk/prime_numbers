import math

n = 10 ** 7
i = 2
ofile = open('output.txt', 'w')
while i < n:
    k = 2
    m = 0
    while k <= int(math.sqrt(i)):
        if i % k == 0:
            m = m + 1
        k = k + 1
    if m == 0:
        ofile.write('{}\n'.format(i))
    i = i + 1
ofile.close()
