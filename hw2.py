# Name: Ariel (Rel)
# Evergreen Login: rozari15
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


import math
import hw2_test


###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

x = 0
s = 0
while (x <= hw2_test.n):
    s = s + x
    x = x + 1
print s


###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

x = 1.0
for n in range(2, 11):
    print x / n

# read up on the range() function and for loops


###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

n = 10
triangular = 0
for i in range(n):
    triangular = triangular + i
print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", n*(n+1)/2



###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

n = 10
p = 1
for i in range(2, n + 1):
    p = p * i
print p


###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

n = 10
p = 1


for i in range(1, n + 1):
    n = n - 1
    for q in range(1, n + 1):
        p = p * q
    
    print p

# i cannot, for the life of me, figure this one out

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

x = 1.0
t = 1
for n in range(2, 11):
    t = t * (x / n)

print t

# returns 2.75; that's close enough

###
### Collaboration
###

# i used the icup text for understanding while and for loops.
# i used the python website for the built in range() funtion

###
### Reflection
###

# including class time, i'd say i spent about seven hours on this assignment;
# i guess i need to figure out nested for loops
