import numpy as np
import matplotlib.pyplot as plt
x= np.arange(1,10)
y= 2*x+5  #bodmas concept
print(y)
plt.title("plot demo using expresion") #title of the plot
plt.xlabel("x-axis = 1 to 10")
plt.ylabel("y axis = (2*x+5)")
plt.ylim(1,25)
plt.xlim(1,10)   #to set axis limit
plt.plot(x,y,color = 'g',linestyle='dashed', marker='o', markerfacecolor='pink',)  #formatting
# ob =to get circular dot representation
plt.show()



