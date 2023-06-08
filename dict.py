myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#print(myfamily)
for (x,y) in myfamily.items():
 print(x,y)

# initialise dict with key and then add values
x = ['name', 'age', 'gender']
print(type(x))
thisdict = dict.fromkeys(x)
thisdict['name'] = "divya"
print(thisdict)
print(type(thisdict))

import module as mo
mo.greeting("divya")


a=mo.person1["age"]
print(a)

for x,y in mo.person1.items():
  print(x,y)

d = dir({mo})
print(d)

from module import person1 as pa
if "age" in pa:
  print("true")

help(print)
help(string)
import functools as ft
help(ft)

