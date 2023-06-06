'''
* conditional statements are also called as "Decision-making condition".

* conditional statements are:
if , else , elif , nested if.

syntax:

if condition:
    statement
else
    statement

'''

# if True:
#     print("Hi")
# else:
#     print("Bye")

# if False:
#     print("Hi")
# elif True:
#     print("elif")
# else:
#     print("Bye")

if True:
    print("outer if")

    if True:
        print("inner if")
    else:
        print("inner else")
else:
    print("outer else")

# if True:
#     print("outer if")

#     if False:
#         print("inner if")
#     else:
#         print("inner else")
# else:
#     print("outer else")

# if False:
#     print("outer if")

#     if False:
#         print("inner if")
#     else:
#         print("inner else")
# else:
#     print("outer else")

# age = 19
# if age>18:
#     print("you can vote")
# elif age == 18:
#     print("You can vote buddy")
# else:
#     print("wait")

#logical operator

# age = 18
# if age > 18 or age == 18:
#     print("you can vote")
# else:
#     print("wait")