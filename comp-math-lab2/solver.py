from functions import derivative, check_if_monotonic,check_if_not_equals_zero,partial_derivative
from visualizer import draw_function,draw_answ
from output_handler import print_root_exists,print_number_of_roots,print_speed,print_if_converges
import numpy as np
def solve(method,left,right,f):
    if(check_if_root_exists_on_inteval(left,right,f)):
        print_root_exists()
        print_number_of_roots(check_if_root_is_unique(f,left,right))
    match method:
        case "Newton":
            print_if_converges(check_if_converge_with_newton(f,left,right))
            begin = find_start_for_newton(f,left,right)

            print_speed(begin[1])

            answ  = newton(f,begin[0],0.001)
            print(answ)

            draw_function(f, left-left*2,right+right*2)
            draw_answ(newton(f,begin[0],0.001))
        case "Secant":
            print_if_converges(check_if_converge_with_newton(f,left,right))
            begin=find_start_for_newton(f,left,right)
        
            print_speed(begin[1])


            answ = secant(f,begin[0],begin[0]+0.01,0.001)
            print(answ)


            draw_function(f, left-left*2,right+right*2)
            draw_answ(secant(f,begin[0],begin[0]+0.01,0.001))
        
   
def solve_systems(system,x0):
    if(check_if_converge_with_fixed_point(system,x0)):
            
            print("Сойдётся по точке")
    print(fixed_point_iteration(system,x0,0.001))


def compute_phi_i_for_fixed_point_iteration(system,x,i,lambd):
    return (-1/lambd)*system(x)[i]+x[i]
def compute_phi_for_fixed_point_iteration(f,x):
    return np.array([compute_phi_i_for_fixed_point_iteration(f,x,i,find_maximum_of_partial_derivative_on_R(f,x,i)) for i in range(len(f(x)))])
def fixed_point_iteration(f,x0,tol):
    x=x0
    while(abs(x-compute_phi_for_fixed_point_iteration(f,x)).all()>tol):
        x=compute_phi_for_fixed_point_iteration(f,x)
    return x


def find_maximum_of_partial_derivative_on_R(f,x,i):
    tmp=partial_derivative(lambda x: f(x)[i],x,i)
    for j in range(-100,100):
        if(partial_derivative(lambda x: f(x)[i],x+j,i)>tmp):
            tmp=partial_derivative(lambda x: f(x)[i],x+j,i)
    return tmp
def check_if_converge_with_fixed_point(f,x):
    for i in range(len(f(x))):
        if(find_maximum_of_partial_derivative_on_R(f,x,i)>=1):
            print(find_maximum_of_partial_derivative_on_R(f,x,i))
            return False
    return True
     


def check_if_root_exists_on_inteval(left, right, f):
    if f(left) * f(right) > 0:
        return False
    return True
def secant(f, x0, x1, tol):
    x = x1
    while abs(f(x)) > tol:
        x = x - f(x)*(x-x0)/(f(x)-f(x0))
        x0 = x1
        x1 = x
    return x
def newton(f, x0, tol):
    x = x0
    while abs(f(x)) > tol:
        x = x - f(x)/derivative(f,x)
    return x
def find_start_for_newton(f, left, right):
    if(f(left)*derivative(lambda x: derivative(f,x),left)>0):
        return [left,True]
    if(f(right)*derivative(lambda x: derivative(f,x),right)>0):
        return [right,True]
    return [left,False]

def check_if_root_is_unique(f,left,right):
    return (check_if_monotonic(f,left,right) and check_if_root_exists_on_inteval(left,right,f))

def check_if_converge_with_newton(f,left,right):
    return check_if_monotonic(f,left,right) and check_if_monotonic(lambda x: derivative(f,x), left,right)