import sympy as sp
from beautifultable import BeautifulTable
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import numpy as np
import math
booleann_log = True
booleann_exp = True
booleann_pow = True
def inputn():

        n = input()
        try:
                n=int(n)
        except:
                print("Введите целое число")
                inputn()
        return n
def inputx(n):
        x=[]
        print("Введите значения x")
        for i in range(n):
                x=input()
                try:
                        x.append(float(x))
                except:
                        print("Введите число")
                        inputx(n)
        return x
def inputy(n):
        y=[]
        print("Введите значения y")
        for i in range(n):
                y=input()
                try:
                        y.append(float(y))
                except:
                        print("Введите число")
                        inputy(n)
        return y


def create_polynomial(n):
    x = sp.symbols('x')
    coefficients = sp.symbols('a0:%d' % (n+1))
    polynomial = sum(coefficients[i] * x**i for i in range(n+1))
    polynomial_expanded = sp.expand(polynomial)
    return polynomial_expanded

def leastSquares(n):
    x, y = sp.symbols('x y')
    f_i = create_polynomial(n) - y
    f_i = f_i**2
    f_i = sp.expand(f_i)

    # Create a list of coefficient symbols
    coefficients = sp.symbols('a0:%d' % (n+1))

    # Compute the partial derivatives with respect to the coefficients
    derivatives = [f_i.diff(coeff) for coeff in coefficients]

    return derivatives;
def linear_regression(x,y):
        x_symbol=sp.symbols('x')
        n = len(x)
        sx=sum(x)
        sy=sum(y)
        sxy=sum([x[i]*y[i] for i in range(n)])
        sxx=sum([x[i]**2 for i in range(n)])
        a0,a1,a2=sp.symbols('a0,a1,a2')
        eq1=a0*n+a1*sx-sy
        eq2=a0*sx+a1*sxx-sxy
        a=sp.solve([eq1,eq2],[a0,a1])
        return sp.expand(a[a0]+a[a1]*x_symbol),a
        
        
def quadratic_regression(x,y):
        x_symbol=sp.symbols('x')
        n=len(x)
        sx=sum(x)
        sy=sum(y)
        sxy=sum([x[i]*y[i] for i in range(n)])
        sxx=sum([x[i]**2 for i in range(n)])
        sxxx=sum([x[i]**3 for i in range(n)])
        sxxxx=sum([x[i]**4 for i in range(n)])
        sxxy=sum([x[i]**2*y[i] for i in range(n)])
        print("sx = " + str(sx))
        print("sxx ="  +  str(sxx))
        print("sxxx = " + str(sxxx))
        print("sxxxx =" +  str(sxxxx))
        print("sxxy = " + str(sxxy))

        a0,a1,a2=sp.symbols('a0,a1,a2')
        eq1=a0*n+a1*sx+a2*sxx-sy
        eq2=a0*sx+a1*sxx+a2*sxxx-sxy
        eq3=a0*sxx+a1*sxxx+a2*sxxxx-sxxy
        a=sp.solve([eq1,eq2,eq3],[a0,a1,a2])

        
        return sp.expand(a[a0]+a[a1]*x_symbol+ a[a2]*x_symbol**2),a


def cubic_regression(x,y):
        x_symbol=sp.symbols('x')
        n=len(x)
        sx=sum(x)
        sy=sum(y)
        sxy=sum([x[i]*y[i] for i in range(n)])
        sxx=sum([x[i]**2 for i in range(n)])
        sxxx=sum([x[i]**3 for i in range(n)])
        sxxxx=sum([x[i]**4 for i in range(n)])
        sxxxxx=sum([x[i]**5 for i in range(n)])
        sxxxxxx=sum([x[i]**6 for i in range(n)])
        sxxy=sum([x[i]**2*y[i] for i in range(n)])
        sxxxy=sum([x[i]**3*y[i] for i in range(n)])
        a0,a1,a2,a3=sp.symbols('a0,a1,a2,a3')
        eq1=a0*n+a1*sx+a2*sxx+a3*sxxx-sy
        eq2=a0*sx+a1*sxx+a2*sxxx+a3*sxxxx-sxy
        eq3=a0*sxx+a1*sxxx+a2*sxxxx+a3*sxxxxx-sxxy
        eq4=a0*sxxx+a1*sxxxx+a2*sxxxxx+a3*sxxxxxx-sxxxy
        a=sp.solve([eq1,eq2,eq3,eq4],[a0,a1,a2,a3])
        return sp.expand((a[a0]+a[a1]*x_symbol+ a[a2]*x_symbol**2+a[a3]*x_symbol**3)),a
        
def exponential_function_regression(x,y):
        x_symbol=sp.symbols('x')
        n=len(x)
        sx=sum(x)
        sy=sum([sp.log(y[i]) for i in range(n)])
        sxy=sum([x[i]*sp.log(y[i]) for i in range(n)])
        sxx=sum([x[i]**2 for i in range(n)])
        a0,a1=sp.symbols('a0,a1')
        eq1=a0*n+a1*sx-sy
        eq2=a0*sx+a1*sxx-sxy
        a=sp.solve([eq1,eq2],[a0,a1])
        a[a0]=sp.exp(a[a0])
        return sp.expand(a[a0]*sp.exp(a[a1]*x_symbol)),a
       
def logarithmic_function_regression(x,y):
        x_symbol=sp.symbols('x')
        n=len(x)
        sx=sum([sp.log(x[i]) for i in range(n)])
        sy=sum(y)
        sxy=sum([sp.log(x[i])*y[i] for i in range(n)])
        sxx=sum([sp.log(x[i])**2 for i in range(n)])
        a0,a1=sp.symbols('a0,a1')
        eq1=a0*n+a1*sx-sy
        eq2=a0*sx+a1*sxx-sxy
        a=sp.solve([eq1,eq2],[a0,a1])
        return sp.expand(a[a0]+a[a1]*sp.log(x_symbol)),a
def power_function_regression(x,y):
        x_symbol=sp.symbols('x')
        n=len(x)
        sx=sum([sp.log(x[i]) for i in range(n)])
        sy=sum([sp.log(y[i]) for i in range(n)])
        sxy=sum([sp.log(x[i])*sp.log(y[i]) for i in range(n)])
        sxx=sum([sp.log(x[i])**2 for i in range(n)])
        a0,a1=sp.symbols('a0,a1')
        eq1=a0*n+a1*sx-sy
        eq2=a0*sx+a1*sxx-sxy
        a=sp.solve([eq1,eq2],[a0,a1])
        a[a0]=sp.exp(a[a0])
        return sp.expand(a[a0]*x_symbol**a[a1]),a
def deriv(x,y,f):
        summ=0

        for i in range(len(x)):

                summ+=(f.subs('x',x[i])-y[i])**2
        return summ,math.sqrt(summ/len(x))
def correlation_coefficient(x,y):
        x_mean=sum(x)/len(x)
        y_mean=sum(y)/len(y)
        x_new=[x[i]-x_mean for i in range(len(x))]
        y_new=[y[i]-y_mean for i in range(len(y))]
        return sum([x_new[i]*y_new[i] for i in range(len(x))])/math.sqrt(sum([x_new[i]**2 for i in range(len(x))])*sum([y_new[i]**2 for i in range(len(y))]))
def printy():
        a0,a1,a2,a3=sp.symbols('a0,a1,a2,a3')

        
        table=PrettyTable(['function','a','b','c', 'd', 'Мера отклонения S','Среднеквадратичное отклонение'])
        table.add_row(['Линейная',linear_regression(x,y)[1][a1],linear_regression(x,y)[1][a0],'-','-',deriv(x,y,linear_regression(x,y)[0])[0],deriv(x,y,linear_regression(x,y)[0])[1]])
        table.add_row(['Степенная',power_function_regression(*filter_xy(x,y))[1][a0],power_function_regression(*filter_xy(x,y))[1][a1],'-','-',        deriv(*filter_xy(x,y),power_function_regression(*filter_xy(x,y))[0])[0],deriv(*filter_xy(x,y),power_function_regression(*filter_xy(x,y))[0])[1]])
        table.add_row(['Экспоненциальная',exponential_function_regression(*filter_y(x,y))[1][a0],exponential_function_regression(*filter_y(x,y))[1][a1],'-','-',deriv(*filter_y(x,y),exponential_function_regression(*filter_y(x,y))[0])[0],deriv(*filter_y(x,y),exponential_function_regression(*filter_y(x,y))[0])[1]])
        table.add_row(['Логарифмическая',logarithmic_function_regression(*filter_x(x,y))[1][a1],logarithmic_function_regression(*filter_x(x,y))[1][a0],'-','-',deriv(*filter_x(x,y),logarithmic_function_regression(*filter_x(x,y))[0])[0],deriv(*filter_x(x,y),logarithmic_function_regression(*filter_x(x,y))[0])[1]])
        table.add_row(['Квадратичная',quadratic_regression(x,y)[1][a2],quadratic_regression(x,y)[1][a1],quadratic_regression(x,y)[1][a0],'-',deriv(x,y,quadratic_regression(x,y)[0])[0],deriv(x,y,quadratic_regression(x,y)[0])[1]])
        table.add_row(['Кубическая',cubic_regression(x,y)[1][a3],cubic_regression(x,y)[1][a2],cubic_regression(x,y)[1][a1],cubic_regression(x,y)[1][a0],deriv(x,y,cubic_regression(x,y)[0])[0],deriv(x,y,cubic_regression(x,y)[0])[1]])
        print(table)
def filter_x(x,y):
        global booleann_log

        x_new=[]
        y_new=[]
        for i in range(len(x)):
                if(x[i]<=0):
                        if(booleann_log):
                                print("Внимание! В функции логарифмической регрессии x должен быть больше 0")
                                booleann_log = False
                        continue
                else:
                        x_new.append(x[i])
                        y_new.append(y[i])
        return [x_new,y_new]
def filter_y(x,y):
        global booleann_exp

        x_new=[]
        y_new=[]
        for i in range(len(x)):
                if(y[i]<=0):
                        if(booleann_exp):
                                print("Внимание! В функции экспоненциальной регрессии y должен быть больше 0")
                                booleann_exp = False

                        continue
                else:
                        x_new.append(x[i])
                        y_new.append(y[i])
        return [x_new,y_new]
def filter_xy(x,y):
        global booleann_pow

        x_new=[]
        y_new=[]
        for i in range(len(x)):
                if(x[i]<=0 or y[i]<=0):
                        if(booleann_pow):
                                print("Внимание! В функции степенной регрессии x и y должны быть больше 0")
                                booleann_pow = False
                        continue
                else:
                        x_new.append(x[i])
                        y_new.append(y[i])
        return [x_new,y_new]
        
def print_for_method(f):
        table = PrettyTable(['x', 'y', 'phi(x)', 'y-phi(x)'])
        for i in range(len(x_n)):
                table.add_row([x_n[i],y_n[i],f.subs('x',x_n[i]),y_n[i]-f.subs('x',x_n[i])])
        print(table)
def draw(x,y,f):
        plt.plot(x,y,'o')
        x1=np.linspace(min(x),max(x),100)
        y1=[f.subs('x',x1[i]) for i in range(len(x1))]
        plt.plot(x1,y1)
        
def draw_everything():
        plt.title("Все функции")
        draw(x,y,linear_regression(x,y)[0])
        draw(x,y,quadratic_regression(x,y)[0])
        draw(x,y,cubic_regression(x,y)[0])
        draw(*filter_y(x,y),exponential_function_regression(*filter_y(x,y))[0])
        draw(*filter_x(x,y),logarithmic_function_regression(*filter_x(x,y))[0])
        draw(*filter_xy(x,y),power_function_regression(*filter_xy(x,y))[0])
        plt.show()
def find_best():
        s_list=[[deriv(x,y,linear_regression(x,y)[0])[1],linear_regression],[deriv(x,y,quadratic_regression(x,y)[0])[1],quadratic_regression],[deriv(x,y,cubic_regression(x,y)[0])[1],cubic_regression],[deriv(*filter_y(x,y),exponential_function_regression(*filter_y(x,y))[0])[1],exponential_function_regression],[deriv(*filter_x(x,y),logarithmic_function_regression(*filter_x(x,y))[0])[1],logarithmic_function_regression],[deriv(*filter_xy(x,y),power_function_regression(*filter_xy(x,y))[0])[1],power_function_regression]]
        s_list.sort(key=lambda x:x[0])

        return s_list[0];
def draw_best():
        best = find_best()
        name = get_name(best[1].__name__.split('_')[0]) + " функция"
        plt.title("Лучшая функция - " + name)
        draw(x_n,y_n,best[1](x_n,y_n)[0])


def inputall():
        n=inputn()
        x=inputx(n)
        y=inputy(n)
        return x,y
def inputallfromfile(name):
        x,y=[],[]
        with open(name,'r') as f:
                n=int(f.readline())
                for i in range(n):
                        line = f.readline().split()
                        x.append(float(line[0]))
                        y.append(float(line[1]))
                
        return x,y
def get_name(func_name):
        match func_name:
                case 'linear':
                        return 'Линейная'
                case 'quadratic':
                        return 'Квадратичная'
                case 'cubic':
                        return 'Кубическая'
                case 'exponential':
                        return 'Экспоненциальная'
                case 'logarithmic':
                        return 'Логарифмическая'
                case 'power':
                        return 'Степенная'
def functionn():
        print("Хотите исследовать конкретную функцию? (y/n)")
        funct = {"1":linear_regression,"2":quadratic_regression,"3":cubic_regression,"4":exponential_function_regression,"5":logarithmic_function_regression,"6":power_function_regression}
        a=input()
        if a=='y':
                print("1. Линейная")
                print("2. Квадратичная")
                print("3. Кубическая")
                print("4. Экспоненциальная")
                print("5. Логарифмическая")
                print("6. Степенная")
                b=input()
                print("Значение функции в точках:")
                print_for_method(funct[b](x,y)[0])
                a=input("Хотите построить график этой функции? (y/n) ")
                if a=='y':
                        draw(x,y,funct[b](x,y)[0])
                        plt.show()
               
                a = input("Хотите исследовать другую функцию? (y/n)")
                if a=='y':
                        functionn()
def welcome():
        print("Добро пожаловать в программу по поиску функции, наилучшим образом описывающей заданные данные")
        print("Выберите способ ввода данных:")
        print("1. Ввести данные вручную")
        print("2. Загрузить данные из файла")
        a=int(input())
        if a==1:
                x,y=inputall()
        elif a==2:
                name=input("Введите имя файла: ")
                x,y=inputallfromfile(name)
        return x,y
x,y=welcome()
print("Ваши данные:")
print(x)
print(y)
print("Ваша аппроксимирующих функций:")
printy()

print("Из неё видно, что наилучшей функцией является " + get_name(find_best()[1].__name__.split('_')[0]) + " функция")
print("Значения данной функции в точках:")
best =  find_best()[1]
x_n,y_n=x,y
if best.__name__.split('_')[0] == 'power':
        x_n,y_n=filter_xy(x,y)
if best.__name__.split('_')[0] == 'logarithmic':
        x_n,y_n=filter_x(x,y)
if best.__name__.split('_')[0] == 'exponential':
        x_n,y_n=filter_y(x,y)
print_for_method(best(x_n,y_n)[0])

a=input("Хотите построить график этой функции? (y/n) ")
if a=='y':
        draw_best()
        plt.show()
print("Хотите построить график всех функций? (y/n)")
a=input()
if a=='y':
        draw_everything()
        plt.show()
print("Хотите вывести коэффициент линейной регрессии? (y/n)")
a=input()
if a=='y':
        print(correlation_coefficient(x,y))
functionn()
print("До свидания!")



       
