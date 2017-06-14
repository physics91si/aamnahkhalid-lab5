#!/usr/bin/python

#The following statements are used to import numpy and matplotlib.
import numpy as np
import matplotlib.pyplot as plt



# TODO fill in this function
def integrate(y, dx):
    ##using trapezium rule of integration
    return sum([(dx/2)*(y[x]+y[x+1]) for x in range(0,len(y)-1)])

# TODO write code here to setup arrays x and y = sin(x) and then plot them.
x_vals = np.arange(0, np.pi, 0.01) 
sin_x= [np.sin(x) for x in x_vals]
sin_plot = plt.figure()
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.plot(x_vals, sin_x)
plt.savefig('sin_x.png')
# After this is done implement your integrate function above integrate y

print(integrate(sin_x, 0.01)) ##closest estimate when dx is same as the spacing of x_vals

#Cos x
x_vals = np.arange(0, np.pi, 0.01) 
cos_x= [np.cos(x) for x in x_vals]
cos_plot = plt.figure()
plt.xlabel("x")
plt.ylabel("cos(x)")
plt.plot(x_vals, cos_x)
plt.savefig('cos_x.png')

print(integrate(cos_x, 0.01)) ##estimate is close to actual value of 0 when dx is the same as spacing of x_va;s

'Numpy.trapz implements composite trapezoid rule as well'

print(np.trapz(sin_x))
print(np.trapz(sin_x, dx=0.01))#dx is optional parameter. Trapz gives wrong estimate without correct dx
print(np.trapz(cos_x))
print(np.trapz(cos_x, dx=0.01))
