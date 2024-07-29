'''
* String : It is a collection of characters.

* Types of declaring strings:
1. single quote ('')
2. Double quote ("")
3. Triple quote (''' ''')

Methods:

* lower()
* upper()
* endswith()
* startswith()
* replace()
* split()
* strip()
* lstrip()
* rstrip()
* count()
* removeprefix()
* remove suffix()
* find()
* index()

# These are the functions of a string
* isalnum()
* isalpha()
* isdigit()
* islower()
* isupper()
* istitle()
* isspace()

'''

# Declaring strings
a = 'college'
b = "university"
c = '''Home town'''

print(type(a) , type(b) , type(c))

# # K = "hi every one"
# K = "HI EVERY ONE"
# # print(K.upper())
# print(K.lower())

# v = "vijay"
# print(v.endswith('y'))
# print(v.endswith('i'))
# print(v.startswith('v'))
# print(v.startswith('j'))

# s = "vijay"
# print(s.replace("vijay" , "Thalapathy"))

# R = "Thalapathy"
# print(R.index("Thala"))
# print(R.find("Thala"))

# R = "Thalapathy vijay"
# print(R.count('j'))
# print(R.removeprefix('Thalapathy'))
# print(R.removesuffix('vijay'))

# R = "KVSR"
# print(R.split())

# R = "   KVSR"
# # print(R)
# # print(len(R))
# # print(R.strip())
# # print(R.lstrip())

# L = R.strip()
# print(L)

# L = R.lstrip()
# print(L)

# L = R.rstrip()
# print(L)