import math
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import numpy as np
import math 
functions=[lambda x,y: x+y, lambda x,y: y+ (1+x)*y**2, lambda x,y: math.cos(x)*y]
y_f=[lambda x,c: c*math.exp(x)-x-1, lambda x,c: -math.exp(x)/(c+math.exp(x)*x), lambda x,c: c*math.exp(math.sin(x))]
methods_p = {"Euler":1,"Runge-Kote":4,"Milan":4}
def euler_differ_eq(x,y0,h,f):

        y=[y0]
        for i in range(1,len(x)):
                
                y.append(y[i-1]+(h/2)*(f(x[i-1],y[i-1]) + f(x[i],y[i-1]+h*f(x[i-1],y[i-1]))))
        
        return(y)
def print_table(x,y,y_f, f):
        print("Таблица значений (первые 100 значений)")
        y_f=[y_f(i) for i in x[:100]]
        table=PrettyTable()
        table.add_column("i",range(0,min(len(x),100)))

        table.add_column("x",x[:100])
        table.add_column("y",y[:100])
        table.add_column("f(x,y)", [f(x[i],y[i]) for i in range(0,min(len(x),100))])
        table.add_column("Точное решение",y_f)
        table.add_column("Погрешность", [abs(y[i]-y_f[i]) for i in range(0,min(len(x),100))])
        print(table)
def paint_graph(x,y,y_f):
        x_true = np.arange(x[0],x[-1],0.01)
        y_f=[y_f(i) for i in x_true]
        plt.plot(x,y,'r',label='Численное решение')
        plt.plot(x_true,y_f,'b',label='Точное решение')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.show()
def runge_kote4(x,y0,h,f):
        y=[y0]
        for i in range(1,len(x)):
                k1=f(x[i-1],y[i-1])
                k2=f(x[i-1]+h/2,y[i-1]+h/2*k1)
                k3=f(x[i-1]+h/2,y[i-1]+h/2*k2)
                k4=f(x[i-1]+h,y[i-1]+h*k3)
                y.append(y[i-1]+(h/6)*(k1+2*k2+2*k3+k4))
        
        return(y)
def milan_diff_eq(x,y0,h,f):
        
        y=runge_kote4(x[:4],y0,h,f)
        for i in range(4,len(x)):
                y_predict = y[i-4] + (4*h/3)*(2*f(x[i-1],y[i-1])-f(x[i-2],y[i-2])+2*f(x[i-3],y[i-3]))
                y_correct = y[i-2] + (h/3)*(f(x[i-2],y[i-2])+4*f(x[i-1],y[i-1])+f(x[i],y_predict))
                y.append(y_correct)
        return(y)
image.png
def main_method_single_it(x,y0,method,error,p,h,f):
        
        iterations=1
        current = method(x,y0,h,f)
        next = method(np.arange(x[0],x[-1],h/2),y0,h/2,f)
        while(abs(current[-1]-next[-1])/(2**p -1)>error):
                iterations+=1
                h=h/2
                current = method(np.arange(x[0],x[-1]+h,h),y0,h,f)
                next = method(np.arange(x[0],x[-1]+h/2,h/2),y0,h/2,f)
        return(next,iterations,np.arange(x[0],x[-1]+h/2,h/2),abs(current[-1]-next[-1]))

def main_method_multi_it(x,y0, y_true,method,error,p,h,f):
        iterations = 1
        boolean = True
        errorix=error
        while(boolean):
                answ = method(x,y0,h,f)
                boolean=False
                for i in range(len(answ)):
                        if(abs(answ[i]-y_true(x[i]))>error):
                                x=np.arange(x[0],x[-1]+h/2,h/2)
                                iterations+=1
                                h=h/2
                                boolean=True
                                break
                        errorix = min(abs(answ[i]-y_true(x[i])),errorix)
        return(answ,iterations,x,abs(answ[i]-y_true(x[i])),errorix)

def get_method():
        a=[1,2,3]
        print("Выберите метод решения дифференциального уравнения")
        print("1. Метод Эйлера")
        print("2. Метод Рунге-Кутта")
        print("3. Метод Милна")
        method = int(input())
        if(method not in a):
                print("Неверный ввод")
                return(get_method())
        return(method)
def get_error():
        print("Введите погрешность")
        error = float(input())
        if(error<=0):
                print("Неверный ввод")
                return(get_error())
        return(error)
def get_left_border():
        print("Введите левую границу")
        left_border = float(input())
        return(left_border)
def get_right_border():
        print("Введите правую границу")
        right_border = float(input())
        return(right_border)
def get_step():
        print("Введите шаг")
        step = float(input())
        if(step<=0):
                print("Неверный ввод")
                return(get_step())
        return(step)
def get_begin_value():
        print("Введите начальное значение")
        begin_value = float(input())
        return(begin_value)
def choose_f():
        global functions, y_f
        print("Выберите функцию")
        print("1. y'=x+y")
        print("2. y'=y+(1+x)*y^2")
        print("3. y'=y*cos(x)")
        funct = int(input())
        if(funct==1):
                return ([functions[0],y_f[0],1])
        elif(funct==2):
                return([functions[1],y_f[1],2])
        elif(funct==3):
                return([functions[2],y_f[2],3])
        else:
                print("Неверный ввод")
                return(choose_f())
def find_const(y0,x0,i):
        global y_f
        if(i==1):
                return((y0+1+x0)/(math.exp(x0)))
        elif(i==2):
                return((-math.exp(x0)*(x0*y0+1))/y0)
        elif(i==3):
                return(y0/math.exp(math.sin(x0)))

def compare_table(x,y0,true_f,error,step,f):
        
        table = PrettyTable()
        table.field_names=["Метод", "Количество итераций", "Погрешность"]
        euler = main_method_single_it(x,y0,euler_differ_eq,error,methods_p["Euler"],step,f)
        runge = main_method_single_it(x,y0,runge_kote4,error,methods_p["Runge-Kote"],step,f)
        milan = main_method_multi_it(x,y0,true_f,milan_diff_eq,error,methods_p["Milan"],step,f)

        table.add_row(["Метод Эйлера", euler[1], euler[3]])
        table.add_row(["Метод Рунге-Кутта", runge[1], runge[3]])
        table.add_row(["Метод Милна", milan[1], milan[3]])
        print(table)


def welcome():
        
        print("Добро пожаловать в программу для решения дифференциальных уравнений")
        a=choose_f()
        left=get_left_border()
        right=get_right_border()
        step=get_step()
        x=[i for i in np.arange(left,right+step,step)]
        y0=get_begin_value()
        boolean=True
        while(boolean):
                boolean=False
                method = get_method()
                error=get_error()
                
                f=a[0]
                y_f=a[1]
                idx = a[2]
                true_f=lambda arg:y_f(arg,find_const(y0,x[0],idx))
                answ = 0
                if(method==1):
                        answ=main_method_single_it(x,y0,euler_differ_eq,error,methods_p["Euler"],step,f)
                elif(method==2):
                        answ=main_method_single_it(x,y0,runge_kote4,error,methods_p["Runge-Kote"],step,f)
                
                elif(method==3):
                        answ=main_method_multi_it(x,y0,true_f,milan_diff_eq,error,methods_p["Milan"],step,f)
                print("!!! Ответ был найден за ",answ[1]," итераций c погрешностью ",answ[3]," !!!")
                print_table(answ[2],answ[0],true_f,f)
                paint_graph(answ[2],answ[0],true_f)

                print("Хотите сравнить методы? (y/n)")
                if(input()=="y"):
                        compare_table(x,y0,true_f,error,step,f)
                print("Хотите продолжить? (y/n)")
                if(input()=="y"):
                        boolean=True



        
welcome()
        
        

