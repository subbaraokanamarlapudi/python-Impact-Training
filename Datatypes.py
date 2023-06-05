'''
* It is a one type of a value.
* It can be a any datatype.

Datatypes are:

* int
* float
* string
* boolean
* complex


* List
* Tuple
* set
* Dictionary

* Frozenset.
* None.
'''

# Int
a = 10
print(type(a))
print(a)

#float
b = 5.5
print(type(b))
print(b)

#Complex
c = 3+4j
print(type(c))
print(c)

#String
d = "KVSR"
print(type(d))
print(d)

#Bool
e = True
print(type(e))           # (or) we can write as print(True == 1)
print(e)

f = False
print(type(f))      # (or) we can write as print(False == 0)
print(f)


# converting the datatypes.

#float to int
x = 15.56
print(int(x))

#int to float
num = 15
print(float(num))

# int to complex
n = 10
print(complex(n))

a = 5
b = -2
print(complex(a,b))