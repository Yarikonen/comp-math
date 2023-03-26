import math
import numpy as np
def f1(x):
    return (x**2)
def f2(x):
    return( np.sin(x)*x + x**2)
def f3(x):
    return(np.sqrt(x) + x*np.cos(x))
def derivative(f, x):
    
    return((f(x+0.0001)-f(x))/0.0001)

    