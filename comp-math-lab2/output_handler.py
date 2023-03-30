
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
                print("Number of roots is more than 1")
def print_root_exists():
        print("Root exists")
        print_small_gap()
def print_if_converges(bool):
        if(bool):
                print("Converges")
        else:
                print("Doesn't converge")
