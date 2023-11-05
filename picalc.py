import numpy as np


a=np.arange(1,1000000,1)
b=np.arange(1,1000000,1)

approximations=[]
n=int(input("Accuracy; "))

pi='3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'

pie=float(pi[0:n+2])
nn=n*-1

error=10**nn

#pi is between 3.141593 and 3.141592
#increment a
#keep incrementing b until you find i/j between the above 2 values
#store only the nearest one to poss along with i and j [app,i,j] format
#stop incrementing the denominator(j) when value of i/j falls below 3.14
#pull closest approximation from approximation list

for i in a:
    for j in b:
        if pie+error>i/j>pie-error:
            print(i/j,i,j)
            approximations.append([i/j,i,j])
        elif i/j<3.14:
            break

print(approximations)
