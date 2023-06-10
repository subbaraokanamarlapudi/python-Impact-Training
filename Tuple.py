'''
* It is one of the datatype.
* It is represented by "()".
* It allows different types of elements.
* It allows duplicates.
* It allows indexing and slicing.
* It is immutable. -----> Data cannot modify.
* No methods. We can use in-bulit functions.

* In-bult functions are : -----> max,min,sum,zip,len.....

Tuple operations:
* concatentaion.
* Iteration.
* Membership operation.
* Identity operation.
* Repetation.

'''

c = ()
print(type(c))

c = (1,23,1,3,14,"Triangle")
print(c)
print(c[4])
print(c[-1])
print(c[0:4:2])

# In-bulit
# c = (1,99,100,14,50,75,44,55,60)
# print(min(c))
# print(max(c))
# print(len(c))
# print(sum(c))
# print(zip(c))         # It give the address value.

#operations.

#concatation.
# t1 = (1,2,3)
# t2 = (4,5,6)
# print(t1+t2)

# # repeation
# c = (1,23,1,3,14,"Triangle")
# print(c*2)
# print(c*11)

# Iteration

# t = (1,24,1,3,4,14,15,900)
# for i in t:
#     print(i)

# # membership

# print(1 in t)
# print(11 in t)
# print(14 in t)
# print(24 not in t)

# identity operation
# t1 = (1,2,3)
# t2 = (1,2,3)
# print(t1 and t2)
# print(t1 is t2)

# t1 = (1,2,3)
# t2 = (1,2,4)

# print(t1 is t2)