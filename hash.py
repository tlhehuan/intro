import math

p=14
m=2**p
w=32
A=(math.sqrt(5) - 1) / 2


def h(k):
        return int(m * (k * A %1))

print h(123456)
