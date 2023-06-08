# to modify tuple element
t = ("rose", "jasmine", "lotus")
l = list(t)    # converting tuple into list to make changes
print(l)
l.append("sunflower")
t = tuple(l)
print(t)
x = t.index("sunflower")
print(x)

# to unpack tuple
t1 = ("rose", "jasmine", "lotus", "lily")
(x, y, z, p) = t1
print(x,y,z,p)

