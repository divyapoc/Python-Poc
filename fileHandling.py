# file handling to read , write, apend, delete , create
# create file
# file = open("file.txt","x")
# if you try to create already existing file then it throws err
# f = open("myfile.txt","x")
# to read file
file = open("file.txt")
f = open("myfile.txt")

# to read specfic range of character
print(file.read(5))
print(file.read())  # prints leftover text
# to read linewise
f = open("myfile.txt")
print("firstline=",f.readline())
# print(f.readline())

# looping through file text
for x in f:
    print(x)
# writing/append
c = open("file.txt","a")
c.write("Nothing is impossible. The word itself says I'm possible!")
# write- it will overwrite all text in existing file

d= open("file.txt","w")
d.write( "Keep your face always toward the sunshine, and shadows will fall behind you.\n - Walt Whitman")
d.close()  # to close file

# delete file
#file1 = open("samplefile.txt","x")
import os
file1 = open("samplefile.txt","w")
file1.write("to delete a file, you must import the OS module")
file1.close()
os.remove("samplefile.txt")






