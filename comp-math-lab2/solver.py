from functions import derivative, check_if_monotonic,partial_derivative
from visualizer import draw_function,draw_answ,draw_implicit_function
from output_handler import print_root_exists,print_number_of_roots,print_speed,print_if_converges,print_answ
import numpy as np
def solve(method,left,right,f,start=0):
    if(check_if_root_exists_on_inteval(left,right,f)):
        print_root_exists()
        print_number_of_roots(check_if_root_is_unique(f,left,right))
    match method:
        case "Newton":
            print_if_converges(check_if_converge_with_newton(f,left,right))
            begin = find_start_for_newton(f,left,right)

            print_speed(begin[1])

            answ  = newton(f,begin[0],0.001)[0]
            iteration = newton(f,begin[0],0.001)[1]
            print_answ(answ,iteration,f(answ))

            draw_function(f, answ-10,answ+10)
            draw_answ(answ,0)
        case "Secant":
            print_if_converges(check_if_converge_with_newton(f,left,right))
            begin=find_start_for_newton(f,left,right)
        
            print(begin[0])
            print_speed(begin[1])
            


            answ = secant(f,begin[0],begin[0]+0.01,0.001)[0]
            iteration=secant(f,begin[0],begin[0]+0.01,0.001)[1]
            print_answ(answ,iteration,f(answ))
          


            draw_function(f, answ-10,answ+10)
            draw_answ(answ,0)
        case "Fixed point iteration":
            
            print_if_converges(check_if_equation_converge_with_fixed_point(f,start, left,right))

            answ = fixed_point_iteration(f,start,0.001,left,right)[0]
            iteration = fixed_point_iteration(f,start,0.001,left,right)[1]
            
            print_answ(answ,iteration,f(answ))

            draw_function(f, answ-10,answ+10)
            draw_answ(answ,0)

        
   
def solve_systems(system,left,right, x0):
    print_if_converges(check_if_converge_with_fixed_point(system,x0,left,right))

    answ = fixed_point_iteration_system(system,x0,0.001,left,right)[0]
    iteration = fixed_point_iteration_system(system,x0,0.001,left,right)[1]
    print_answ(answ,iteration,system(answ))
    
    draw_implicit_function(system,answ[0]-5, answ[0]+5)

    draw_answ(answ[0],answ[1])

def compute_phi_for_equation(f,x,left,right,begin):
    return (-1/find_maximum_of_equation_partial_derivative_on_R(f,begin,left,right))*f(x)+x

def compute_phi_i_for_fixed_point_iteration(system,x,i,lambd):
    return (-1/lambd)*system(x)[i]+x[i]
def compute_phi_for_fixed_point_iteration(f,x,left,right,begin):
    return np.array([compute_phi_i_for_fixed_point_iteration(f,x,i,find_maximum_of_partial_derivative_on_R(f,begin,i,left,right)) for i in range(len(f(x)))])
def fixed_point_iteration_system(f,x0,tol,left,right):
    begin=x0
    x=x0
    i=0
    #while(np.abs(x-compute_phi_for_fixed_point_iteration(f,x,left,right,begin)).any()>tol):
    while(check_everything(np.abs(x-compute_phi_for_fixed_point_iteration(f,x,left,right,begin)),tol)):
    
        print(np.abs(x-compute_phi_for_fixed_point_iteration(f,x,left,right,begin)))
        x=compute_phi_for_fixed_point_iteration(f,x,left,right,begin)
        i+=1
        if(i>1000):
            break

    return x,i,False
def check_everything(array,value):
    for i in range(len(array)):
        if(array[i]>=value):
            return True
    return False
def fixed_point_iteration(f,x0,tol,left,right):
    begin=x0
    x=x0
    i=0
    # while(np.abs(x-compute_phi_for_equation(f,x,left,right))>tol):
    while(np.abs(f(x))>tol):
        i+=1
        x=compute_phi_for_equation(f,x,left,right,begin)
    
    return x,i


def find_maximum_of_partial_derivative_on_R(f,x,i,left,right):
    tmp=partial_derivative(lambda x: f(x)[i],x,i)
    
    for j in range(left,right):
    
        if(partial_derivative(lambda x: f(x)[i],x+j,i)>tmp):
            tmp=partial_derivative(lambda x: f(x)[i],x+j,i)
    return tmp
def find_maximum_of_equation_partial_derivative_on_R(f,x,left,right):
    tmp=derivative(f,x)

    for j in range(left,right):
    
        if(derivative(f,x+j)>tmp):
            tmp=derivative(f,x+j)
    return tmp
def check_if_converge_with_fixed_point(f,x,left,right):
    for i in range(len(f(x))):
        if(find_maximum_of_partial_derivative_on_R(lambda x: compute_phi_for_fixed_point_iteration(f,x,left,right,x),x,i,left,right)>=1):
            print(find_maximum_of_partial_derivative_on_R(lambda x: compute_phi_for_fixed_point_iteration(f,x,left,right,x),x,i,left,right))
            return False
    return True
def check_if_equation_converge_with_fixed_point(f,x,left,right):
    if(find_maximum_of_equation_partial_derivative_on_R(lambda x: compute_phi_for_equation(f,x,left,right,x),x,left,right)>=1):
        print(find_maximum_of_equation_partial_derivative_on_R(lambda x: compute_phi_for_equation(f,x,left,right,x),x,left,right))
        return False
    print(find_maximum_of_equation_partial_derivative_on_R(lambda x: compute_phi_for_equation(f,x,left,right,x),x,left,right))
    return True
   
     


def check_if_root_exists_on_inteval(left, right, f):
    if f(left) * f(right) > 0:
        return False
    return True
def secant(f, x0, x1, tol):
    i=0
    x = x1
    while abs(f(x)) > tol:
        i+=1
        
        x = x - f(x)*(x-x0)/(f(x)-f(x0))
        
        x0 = x1
        x1 = x
    return x,i
def newton(f, x0, tol):
    i=0
    x = x0
    while abs(f(x)) > tol:
        i+=1
        x = x - f(x)/derivative(f,x)
    return x,i
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