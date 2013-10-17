# rel
# rozari15
# lab3
#
# for "fibonacci", compute and print the nth fibonacci number. for "sum",
# compute and print the sum of 3(1) + 3(2) + ... + 3(n). for "neither", print
# "invalid string"


import math
import random

randfib = random.randint(1, 100)
randlist = 1#random.randint(0, 2)
a = 'fibonacci'
b = 'sum'
c = 'neither'

stringList = [a, b, c]

if (randlist == 0):
    print "The", randfib, "th Fibonacci number is:"
    x = 0
    y = 1
    z = 0
    for i in range(randfib + 1):
        x = y
        y = z
        z = x + y
    print z
elif (randlist == 1):
    


