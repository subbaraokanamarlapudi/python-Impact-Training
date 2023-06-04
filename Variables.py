'''
* Variable can store a value.
* It can also show the address of the value.
* value can be any data type[int,float,string,list,tuple,complex........etc].

SYNTAX: variable_name = value

id() ---> it will show the variable of the memory location.

RULES:

* Don't start with digits (or) symbols.
* starting letter should be alphabets and underscore.
* case sensitive.
'''

a = 10
print(a)

b = 3.14
print(b)

c = "KVSR"
print(c)

d = 3+4j
print(d)

a,b,c = 1,3,4
print(a,b,c)

c = 1,2,3
print(c)

c=v=x=22
print(c,v,x)

abc = 3
print(id(abc))

a = 12
A = 21
print(a)
#print(A)