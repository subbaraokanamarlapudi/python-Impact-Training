'''
* It is a datatype.
* It represented by "{}".
* It represents key and values.
* Value should be mutable.
* No slicing.
* keys are unique.

a = {'a':123 , 1:"abc"}

Here,  'a' ----> represents KEY
123 -----> represents values.

Dict methods:
* get()
* update()
* values()
* keys()
* items()
'''

d = {}
print(type(d))

d = {1:'abc' , 22:'KVSR' , "python":1}
print(d)

print(d[22])

#Methods

# d = {1:'abc' , 22:'KVSR' , "python":1}
# print(d.get(1))
# print(d.keys())
# print(d.values())
# print(d.items())

# d = {1:'abc' , 22:'KVSR' , "python":1}
# d.update({1111:2222})
# print(d)

# for i in {1:'abc' , 22:'KVSR' , "python":1}:
#     print(i)

# for i in {1:'abc' , 22:'KVSR' , "python":1}.values():
#     print(i)

# for i,j in {1:'abc' , 22:'KVSR' , "python":1}.items():
#     print(i,j)

# for i in {1:'abc' , 22:'KVSR' , "python":1}.keys():
#     print(i)