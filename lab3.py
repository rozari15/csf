# rel
# rozari15
# lab3
#
# for "fibonacci", compute and print the nth fibonacci number. for "sum",
# compute and print the sum of 3(1) + 3(2) + ... + 3(n). for "neither", print
# "invalid string"


import math
import random

randnum = random.randint(0, 100)
randlist = random.randint(0, 2)
a = 'fibonacci'
b = 'sum'
c = 'neither'

stringList = [a, b, c]

if (randlist == 0):
    if (randnum == 1):
        print "The", randnum, "st Fibonacci number is:"
    elif (randnum == 2):
        print "The", randnum, "nd Fibonacci number is:"
    elif (randnum == 3):
        print "The", randnum, "rd Fibonacci number is:"
    else:
        print "The", randnum, "th Fibonacci number is:"
        x = 0
        y = 1
        z = 0
        for i in range(randnum):
            x = y
            y = z
            z = x + y
        print z
elif (randlist == 1):
    print "The sum of 3(0) + 3(1) + ... + 3(n) is:"
    x1 = 0
    y1 = 1
    for j in range(1, randnum + 1):
        y1 = j * 3
        x1 = x1 + y1
    print x1
else:
    print "Invalid String."
