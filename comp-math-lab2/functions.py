
import numpy as np
def system1(x):
    return np.array([x[0]**3+x[1]*x[0]+8,x[0]+x[1]+4])
def system2(x):
    return( np.array([0.1*x[0]**2+x[0]+0.2*x[1]**2-0.3,0.2*x[0]**2+x[1]+0.1*x[0]*x[1]-0.7]))
def f1(x):
    return ((x+5)**2 + x**3 + x**2 + 1)
def f2(x):
    return( np.sin(x)*x + x**2)
def f3(x):
    return(x*np.sin(x))
def derivative(f, x):
    return((f(x+0.0001)-f(x))/0.0001)
def partial_derivative(f, x, i):

    y=np.array([x[j]+0.0001 if j==i else x[j] for j in range(len(x))])
    return((f(y)-f(x))/0.0001)
def jacobian(f,x):
    return np.linalg.det(np.array([partial_derivative(f,x,i) for i in range(len(x))]))

def check_if_monotonic(f,a,b):

    tmp=derivative(f,a)
    for i in range(a*10,b*10):
        
        if(derivative(f,i/10)*tmp<0):
            return False
    return True
def check_if_not_equals_zero(f,a,b):
    for i in range(a*10,b*10):
        if(f(i)!=0):
            return False
    return True
def get_function_by_index(index):
    if(index==1):
        return f1
    if(index==2):
        return f2
    if(index==3):
        return f3
def get_system_by_index(index):
    if(index==1):
        return system1
    if(index==2):
        return system2
def get_dimensions_of_system_by_index(index):
    if(index==1):
        return 2
    if(index==2):
        return 2
