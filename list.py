# length of list without using len function

list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
i = 0
for x in list1:
    i += 1
print(i)

# append tuple element into list

list3 = ["apple", "banana", "kiwi"]
tuple1 = ("orange", "cherry", "banana")
list3.extend(tuple1)
print(list3)


i= [1,2,3]
k=[4,5,6]
print([x*y for x in i for y in k ])

# condition in comprehension

list4 = ["apple", "banana", "kiwi", "apple", "orange"]
newlist = [x if x != "orange" else "chery" for x in list4]   # prints elements if it is not orange ,if orange prints chery
list6 = [x for x in list4 if "a" not in x]   # prints element if a is not in list elements
print(list6)
print(newlist)
list4.sort(reverse=True)    # to sort in descending order
print(list4)



