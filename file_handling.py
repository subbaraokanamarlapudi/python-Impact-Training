'''
* Reading , Writing , Deleting , Creating a file is called file handling.

open -> open()
Read/Write
close -> close()
'''

s=open('demo.txt' , mode='r')
print(s.read())
s.close()

s=open('demo.txt' , mode='w')
s.write("bye bye")
s.close()

s=open('demo.txt' , mode='a')
s.write("bye bye write")
s.close()

s=open('demo.txt' , mode='r+')
print(s.read())
s.write("r+mode")
s.close()

s=open('demo.txt' , mode='w+')
s.write("w+mode")
print(s.read())
s.close()

s=open('demo.txt' , mode='w+')
s.write("w+mode")
s.seek(0)
print(s.read())
s.close()