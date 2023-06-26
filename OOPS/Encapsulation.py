'''
* Wrapping of variable and methods into a single unit.

Access specifiers.
* public.
* protected.
* protected.

'''

# Examples.

# class demo():
#     __a = 3 # private
#     _b = 4 # public

#     print(__a)
#     print(_b)


class demo():
    def __init__(self , a , b):
        self.__a = a  # private
        self._b = b   # protected.
 
class demo1(demo):
    def output(self):
        print(self._b)

# Because we accessing the protected one. we cannot access the private one.
c = demo1(3,4)
c.output()