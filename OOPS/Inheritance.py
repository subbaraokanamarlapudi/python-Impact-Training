'''
* It is also one pillar of the oopc.
* parent class properties can access by child class.

TYPES:
* Single inheritance.
* Multiple inheritance.
* Multilevel inheritance.
* Hierachical inheritance.
'''

# single level inheritance.

class parent():
    def output(self):
        print("This is a parent")

class child(parent):
    def outputc(self):
        print("This is a child class")

c = child()
c.outputc()
c.output()

# multi-level inheritance.
# class Grandfather():
#     def outputgf(self):
#         print("This is Grandfather.")

# class parent(Grandfather):
#     def output(self):
#         print("This is parent")

# class child(parent):
#     def outputc(self):
#         print("This is child class")

# c = child()
# c.outputc()
# c.output()
# c.outputgf()

# multiple inheritance.

# class father():
#     def outputf(self):
#         print("This is father class")

# class mother():
#     def outputm(self):
#         print("This is mother class")

# class child(father , mother):
#     def outputc(sef):
#         print("This is child class")

# c = child()
# c.outputc()
# c.outputm()
# c.outputf()

# hierachical inheritance.

# class parents():
#     def output(self):
#         print("This is parents class")

# class child1(parents):
#     def outputA(self):
#         print("This is child1 class")

# class child2(parents):
#     def outputB(self):
#         print("This is child2 class")

# c = child1()
# c2 = child2()

# c.outputA()
# c.output()

# c2.outputB()
# c2.output()