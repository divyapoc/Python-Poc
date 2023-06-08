
# using sorted method--but it is unordered
set1 = {"rose", "jasmine", 'sunflower'}
set1 = sorted(set1)
print(set1)
set1 = set(set1)
print(type(set1))
print(set1)


# using sort()
s = {5,2,7,1,8}
l = list(s)
l.sort()
print(l)
l = set(l)
print(l)




