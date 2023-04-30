from output_handler import print_gap,print_small_gap
from functions import get_function_by_index, get_system_by_index,get_dimensions_of_system_by_index
from visualizer import draw_function, draw_implicit_function,show
import solver
import numpy as np
def input_method():
        print_gap()
        print("Choose method:")
        print("1.Newton")
        print("2.Secant")
        print("3.Fixed point iteration")
        print("4.Fixed point iteration for systems")
        try:
                method = int(input())
                print("aboba")
        except ValueError:
                print("Wrong i2nput! Try again")
                input_method()
        
        if(method not in range(1,5)):
                print("ab")
                print("Wrong input! Try again")
                input_method()
        return method
def input_interval():
        print_small_gap()
        print("Input interval:")
        print("Left:")
        left =input()
        try:
                left=  int(left)
        except:
                print("Wrong input! Try again")
                input_interval()
        print("Right:")
        right = (input())
        try:
                left=  int(left)
        except:
                print("Wrong input! Try again")
                input_interval()
        return int(left),int(right)
def choose_function():
        print_small_gap()
        print("Choose function:")
        print("1.x^3 + x^2 + x + 1")
        print("2.sin(x) + x^2")
        print("3.x*sin(x)")
        try:
               func = int(input())
        except:
                print("Wrong input! Try again")
                choose_function()
        if(func not in range(1,4)):
                print("Wrong input! Try again")
                choose_function()
        return func
def choose_system():
        print_small_gap()
        print("Choose system:")
        print("1.x^3+x*y+8=0\n   x+y+4=0")
        print("2. 0.1x^2+x+0.2y^=0.3\n   0.2x^2+y+0.1xy=0.7")
        try:
               func = int(input())
        except:
                print("Wrong input! Try again")
                choose_system()
        if(func not in range(1,3)):
                print("Wrong input! Try again")
                choose_system()
        return func
def input_start():
        print("Input start:")
        try:
                start = float(input())
        except:
                print("Wrong input! Try again")
                input_start()
        return float(start)
def input_start_vector(dimensions):
        print("Input start-vector")
        answ = np.array([])
        for i in range(dimensions):
                try:
                        answ = np.append(answ,float(input(f"Input x{i+1} ")))
                except:
                        print("Wrong input! Try again")
                        input_start_vector(dimensions)
        return answ
def print_answer(answ):
        print("Answer:")
        print(answ)
def complex_input():
       choose_method=input_method()
       match choose_method:
              case 1:
                         func =get_function_by_index(choose_function())
                         draw_function(func,-10 ,10)
                         show()
                         print(*input_interval())
                         solver.solve("Newton",*input_interval(),func)
              case 2:
                        func =get_function_by_index(choose_function())
                        draw_function(func,-10 ,10)
                        show()
                       
                        solver.solve("Secant",*input_interval(),func)
              case 3:
                        func =get_function_by_index(choose_function())
                        draw_function(func,-10 ,10)
                        show()

                        

                        solver.solve("Fixed point iteration",*input_interval(),func, input_start())
                       
              case 4:
                        system = choose_system()
                        draw_implicit_function(get_system_by_index(system),-10,10)
                        show()
                        a = input_interval()
                        print("Input start-vector")
                        solver.solve_systems(get_system_by_index(system),*a, input_start_vector(get_dimensions_of_system_by_index(system)))
              case _: 
                       print("Wrong input! Try again")
                       complex_input()
       continue_input()
def continue_input():
        print("Do you want to continue?")
        print("1.Yes")
        print("2.No")
        try:
                answ = int(input())
        except:
                print("Wrong input! Try again")
                continue_input()
        if(answ not in range(1,3)):
                print("Wrong input! Try again")
                continue_input()
        if(answ==1):
                complex_input()
        
        else:
                print("Goodbye!")