'''
* It is a physical entity.
* We can allocate any no.of objects for a class.
* memory is allocated when object is created.

SYNTAX:

objectname = classname()
* using object we can access methods and variables of a class.

SYNTAX:

objectname.method()
objectname.variable()
'''

class A():
    a = 3
    def output(self):
        print(self.a)

b = A()
c = A()
b.output()
c.output()

class dll():
    a = 3

    def ll(self):
        print(self.a)

b = dll()
c = dll()
b.ll()
c.ll()