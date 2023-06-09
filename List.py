'''
* It is one datatype.
* It represented by "[]".
* It is a mutable datatype.      "Mutable means changeable datatype."
* It stores different types of elements.
* It allows duplicates elements.
* It allows indexing.

Methods:
* append()
* extend()
* Remove()
* pop()
* count()
* index()

For slicing:
[start:stop:skip] ------> short name as s3

Ex: 
a = [1 , 2.2 , "True" , "Python"]
---------> Positive indexing[0,1,2,3]
Negative indexing<-----------------[-1,-2,-3,-4]

'''

v = []
print(type(v))

v = [1,2.2,1545,True,"python",4,1,5,4,6]
print(v)
print(v[4])
print(v[-3])
print(v[0:4:2])

# v = [1,2.2,3,4,2,1,"True","python","False",5,4,1,2]
# v.append("KVSR")
# v.extend([7,8,9,4,5,6,1,2,300])
# print(v)
# print(v.count(1))
# v.remove(2.2)
# print(v)
# v.pop(3)
# print(v)
# print(v.index("True"))

# v.insert(0,"XYZ")
# print(v)

# for i in [1,2,3,4,4,5,1,34,2113]:
#     print(i)