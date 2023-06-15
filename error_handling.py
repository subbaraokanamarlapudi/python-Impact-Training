'''
* Interpting Normal execution of a code is called error (or) exception.
we will handle by using "Error Handling".

SYNATX:

try:
    risk code
except:
    print("Error")
else:
    print("No Error")
finally:
    print("Always")

'''

# try:
#     print('b')
# except:
#     print("Error")
# else:
#     print("No Error")
# finally:
#     print("Always")

try:
    print('b'+33)
except TypeError:
    print("Type Error")
except ValueError:
    print("Value Error")