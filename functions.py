'''
* It is a block of code and set of instructions.
* Run when it's called.
* Reusability.

Synatx:

"def" is a keyword

def function_name(): ---> function definiation
    function body
function.name() -----> function call
'''

# def fun():
#     print("This is a function")
# fun()

def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)

# def fun(a,b,c):
#     print("This is a function" , a , b , c)
# fun(1,2,3)

# def fun(a,b,c):
#     return a + b + c
# print(fun(1,2,3))

# def fun(*a):
#     print("This is a function" , a)
# fun(a=1)

# def fun(**a):
#     print("This is a function" , a)
# fun(a=1 , b=2)

# Nested functions.

# def outer():
#     print("Outer function")

#     def inner():
#         print("Inner function")
#     inner()
# outer()