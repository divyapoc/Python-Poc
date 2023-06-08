#exception handling
try:
    f= open("samplefile.txt")
    print(f.read())
except IOError: #withhout try and except this will throw error
    print("this file doesnot exist ")
else:
    print("no error is found in your code")
a = "good evening"
# block inside else will print when no exception is raised
try:
     print(a.index("o"))
except ValueError:
    print("index() method throw error when the specified value is not in the string")
else:
    print("o is found in the above string")
#finally executes even when exception occurs
try:
    f2 = open("file.txt","r")
    f2.write("adding more content")
except IOError:
    print("access deined")
finally:
    f2.close()

# raise an exception
import numpy as np
s = np.array([(1, 2, 3, 4)])
p = np.array([(4, 5, 6, 4)])
div = s/p
if type(div) is not int:
    raise Exception("It is not a integer value , it can't be accepted in int operation")

