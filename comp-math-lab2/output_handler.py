
from functions import *
import numpy as np
def print_gap():
    print("--------------------------------------------------")
def print_small_gap():
    print("--------------------------")

def print_speed(bool):
        print_small_gap()
        if(bool):
                print("High convergence speed")
        else:            
                print("Low convergence speed")
def print_number_of_roots(bool):
        print_small_gap()
        if(bool):
                print("Number of roots is 1")
        else:
                print("Number of roots may be more than 1")
def print_root_exists():
        print("Root exists")
        print_small_gap()
def print_if_converges(bool):
        if(bool):
                print("Converges nicely")
        else:
                print("Might not converge")
def print_answ(answ, iteration, f_in_answ):
        print("Your answer is: ")
        print(answ)
        if(iteration==1001):
                print("Iterations limit exceeded")
                return
        print(f"Was found in {iteration} iterations")
        print_small_gap()
        print("f(x) in your answer is: ")
        print(f_in_answ)
        print_small_gap()