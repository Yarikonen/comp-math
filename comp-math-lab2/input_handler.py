from output_handler import print_gap,print_small_gap
from functions import get_function_by_index, get_system_by_index,get_dimensions_of_system_by_index
import solver
def input_method():
        print_gap()
        print("Choose method:")
        print("1.Newton")
        print("2.Secant")
        print("3.Fixed point iteration")
        return int(input())
def input_interval():
        print_small_gap()
        print("Input interval:")
        print("Left:")
        left = int(input())
        print("Right:")
        right = int(input())
        return left,right
def choose_function():
       print_small_gap()
       print("Choose function:")
       print("1.f1")
       print("2.f2")
       print("3.f3")
       return int(input())
def choose_system():
        print_small_gap()
        print("Choose system:")
        print("1.system1")
        print("2.system2")
        return int(input())
def print_answer(answ):
        print("Answer:")
        print(answ)
def complex_input():
       choose_method=input_method()
       match choose_method:
              case 1:
                         solver.solve("Newton",*input_interval(),get_function_by_index(choose_function()))
              case 2:
                       solver.solve("Secant",*input_interval(),get_function_by_index(choose_function()))
              case 3:
                        system = choose_system()
                        print("Input x0")
                        solver.solve_systems(get_system_by_index(system),np.array([int(input(f"Input x{i}"))for i in range(get_dimensions_of_system_by_index(system))]))
