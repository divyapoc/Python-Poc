import numpy as np
a = np.array([(1,2,3,4),(4,5,6,7),(8,9,1,1)])
print(a)
print("dimension=",a.ndim) # to find the dimension
print(a.itemsize)
print(a.shape)
print("square root of array a:" , np.sqrt(a))
print(a.reshape(4,3)) # reshapes the array with 4 rows and 3 coulmn
print("3rd element in row1:",a[0,2]) # to print 3rd element in row1
print(a[0:3, 3]) # to exract 4th element from each rows --> slice method
print(a[1:3,2])
b= np.linspace(1,4,10)  # divides range 1-4 in even interval of 10
print(b)

# axis =0=> column and axis=1=> rows
print(a.sum(axis=1))
print(a.sum(axis=0))

c=np.array([(1,2,3,4),(4,5,6,7)], dtype=int)
d=np.array([(1,2,3,4),(4,5,6,7)] , dtype=int)
#mathematical operator
print("sum=",c+d)
print("sub=",c-d)
print("mul=",c*d)
print("div=",c/d)
#to convert multi row into single row
print("array c =",c.ravel())
#hstack and vstack to append array
s=np.array([(1, 2, 3, 4)])
p=np.array([(4, 5, 6, 4)])
r=np.array([(4, 5, 6, 4)])
print(np.hstack((p,r,s)))
print(np.vstack((s,p,r)))