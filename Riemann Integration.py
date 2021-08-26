from math import *
import numpy as np
import scipy.integrate
from mpmath import nsum,inf



Lower_Limit=0
Upper_Limit=1


def F(x):
    #n=5
    return (3*x**3-x**2+2*x-4)/(sqrt(x**2-3*x+2))

f= lambda x: F(x)
ans,error = scipy.integrate.quad(f, Lower_Limit, Upper_Limit)
print('The ans of the integral:', ans)


print('The answer of the integral is Negative; ATM Pin can not be negative Dheru. Hence we can consider ATM pin is 2981 (first four-digit)')
