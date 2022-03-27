"""
In python repeat structure we don't use {} for 
mark the structure, we use ":" for mark the structure and identation, 
a example:

    a = 10
    if a == 10:
        #True#
        print("a is equal 10")
    else:
        #false#
        print("a is not equal 10")

!!Is that easy!!

operators:
==  ## equal
> ## biggest
< ## smaller
>= ## biggest or equal
<= ## smaller or iqual
!= ## diferent 

"""

a = 7
b = 90

# Basic Repeat Structure

if a != 7:
    print("a is not 7")
else:
    print("a is equal 7")

"""-----------------------------------------------------------------"""

# Here we use "or" and "and". Is self explenatory

if a >= 7 and b > 90: 
    print("true")
else:
    print("false")

if a >= 7 or b > 90:
    print("true")
else:
    print("false")

"""------------------------------------------------------------------"""

# Here we use elif (is basic a if with else, basic u can have 3 verification)

if a == 4:
    print("a is equal 4")
elif a <= 7:
    print("a is equal or smaller than 7")
else:
    print("get false")