import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from prettytable import PrettyTable
y=[1.25,2.38,3.79,5.44,7.14]
boolean = True
def lagrange(x,y):
    n=len(x)
    p=np.poly1d([0])
    for i in range(n):
        l=np.poly1d([1])
        for j in range(n):
            if i!=j:
                l=l*np.poly1d([1,-x[j]])/(x[i]-x[j])
        p=p+y[i]*l
    return p
def diff(y):
    diff=[0 for i in range(len(y)-1)]
    for i in range(len(y)-1):
        diff[i]=y[i+1]-y[i]
    
    return diff
def get_diff_table(x,y):
    diff_table = PrettyTable()
    diff_table.add_column('x', x)
    print(diff_table)
    diff_table.add_column('y', y)
    for i in range(1,len(y)):
        y=diff(y)
        g=y.copy()
        for j in range(len(y),len(x)):
            g.append("-")
        diff_table.add_column(f'Δy_{i}', g) 
    print(diff_table)
def get_all_diff(x,y):
    answ = [[] for i in range(len(y))]
    for i in range(0,len(x)):
    
        for j in range(len(y)):
            answ[j].append(y[j])
        y=diff(y)    
    return answ



def newton_method(argument,x,y):
    min = 100000
    if(argument< (-x[0]+x[-1]/2)):
        index = 0
        for i in range(len(x)):
            if(argument-x[i]<min and argument-x[i]>0):
                min = argument-x[i]
                index = i
        diff = get_all_diff(x,y)[index]
        t=(argument-x[index])/(x[1]-x[0])
        return newton_polynomial(x,y,t,diff,1)
    else:
        
        t = (argument-x[-1])/(x[1]-x[0])
        diff=[]
        for i in get_all_diff(x,y)[::-1]:
            diff.append(i[-1])
    

        return newton_polynomial(x,y,t,diff,-1)
def steerling_interpolation(argument,x,y):
    t=(argument-x[len(x)//2])/(x[1]-x[0])
    print(t)
    diffs=get_all_diff(x,y)
    print(t)
    change = len(x)//2
    answ=0
    j =0
    for i in range(len(x)-(len(x)-1)%2):
        if(i%2==0):
            l=1
            for k in range(i//2):
                
                l*=(t**2-k**2)
            print(diffs[change-j][i])
            answ+=diffs[change-j][i]*l/(np.math.factorial(i))
        else:
            l=t
            print(diffs[change-j-1][i])
            print(diffs[change-j][i])
            for k in range(1,i//2):
                
                l*=(t**2-k**2)
            
            answ+=(diffs[change-j-1][i]+diffs[change-j][i])*l/(2*(np.math.factorial(i)))
            j+=1
    return answ
def bessel_interpolation(argument,x,y):
    t=(argument-x[len(x)//2-(len(x)+1)%2])/(x[1]-x[0])
    diffs=get_all_diff(x,y)
    change = len(x)//2
    if(len(x)%2==0):
        change-=1
    answ=0
    j =-1
    for i in range(len(x)-len(x)%2):
        
        if(i%2==0):
            l=1
            for k in range(0, i//2):
                l*=(t-k)*(t+k-1)
            answ+=(diffs[change-j][i]+diffs[change-j-1][i])*l/(2*np.math.factorial(i))
        
            j+=1
        else:
            l=t-1/2
            for k in range(0, i//2):
                l*=(t-k)*(t+k-1)
            answ+=(diffs[change-j][i])*l/((np.math.factorial(i)))
           
    return answ



def newton_polynomial(x,y,t,diff,k):
    p = 0
    for i in range(len(diff)):
        l = 1
        for j in range(i):
            l = l*(t-k*j)
        p = p + (diff[i]*l)/np.math.factorial(i)
    return p
def draw_lagrange(x,y):
    x1=np.linspace(x[0],x[-1],100)
    y1=lagrange(x,y)(x1)
    plt.plot(x1,y1, label='lagrange')
    plt.legend()
    plt.grid(True)
def draw_points(x,y):
    plt.plot(x,y,'o')
def draw_newton(x,y):
    x1=np.linspace(x[0],x[-1],100)
    y1=[0 for i in range(len(x1))]
    t=(x1-x[0])/(x[1]-x[0])
    for i in range(len(x1)):
        y1[i]=newton_polynomial(x,y,t[i],get_all_diff(x,y)[0],1)
    plt.plot(x1,y1, label='newton')
    plt.legend()
    plt.grid(True)
def draw_stirling(x,y):
    x1=np.linspace(x[0],x[-1],100)
    y1=[0 for i in range(len(x1))]
    for i in range(len(x1)):
        y1[i]=steerling_interpolation(x1[i],x,y)
    plt.plot(x1,y1, label='stirling')
    plt.legend()
    plt.grid(True)
def draw_all(x,y):
    draw_points(x,y)
    draw_bessel(x,y)
    draw_lagrange(x,y)
    draw_newton(x,y)
    draw_stirling(x,y)
    plt.show()
def draw_bessel(x,y):
    x1=np.linspace(x[0],x[-1],100)
    y1=[0 for i in range(len(x1))]
    for i in range(len(x1)):
        y1[i]=bessel_interpolation(x1[i],x,y)
    plt.plot(x1,y1, label='bessel')
    plt.legend()
    plt.grid(True)

def get_n():
    try:
        n=int(input("Введите количество точек: "))
    except:
        print("Неверный ввод")
        get_n()
    return n
def getX(n):
    try:
        x=[float(input(f"Введите x_{i}: ")) for i in range(n)]
    except:
        print("Неверный ввод")
        getX()
    return x
def getY(n):
    try:
        y=[float(input(f"Введите y_{i}: ")) for i in range(n)]
    except:
        print("Неверный ввод")
        getY()
    return y
def getMethod():
    method=0
    try:
        print("1 - Многочлен Лагранжа")
        print("2 - Многочлен Ньютона")
        print("3 - Интерполяционный многочлен Ньютона в форме Стирлинга")
        print("4 - Интерполяционный многочлен Ньютона в форме Бесселя")
        method=int(input("Выберите метод интерполяции: "))

        if method!=1 and method!=2 and method!=3 and method!=4:
            raise Exception
    except:
        print("Неверный ввод")
        getMethod()
    return method
def getArgument():
    try:
        argument=float(input("Введите аргумент: "))
    except:
        print("Неверный ввод")
        getArgument()
    return argument

def welcome():
    print("Добро подаловать в программу по интерполяции функций")
    print("Как хотите ввести данные? (1 - вручную, 2 - из файла, 3 - сгенерировать)")
    k = input()
    method=1
    x=[]
    y=[]
    n=0
    if k=="1":
        n=get_n()
        x=getX(n)
        y=getY(n)
    elif k=="2":
        print("Введите название файла")
        filename=input()
        try:
            f=open(filename,'r')
            n=int(f.readline())
            x=[float(i) for i in f.readline().split()]
            y=[float(i) for i in f.readline().split()]
        except:
            print("Неверный ввод")
            welcome()
    elif k=="3":
        print("Выберите функцию:")
        print("1 - sin(x)")
        print("2 - x^2")
        print("3 - sqrt(x)")
        function = input()
        print("Введите количество точек")
        n=int(input())
        x=[0 for i in range(n)]
        print("Введите левую границу")
        a=float(input())
        print("Введите правую границу")
        b=float(input())
        x=np.linspace(a,b,n)
        if function=="1":
            y=np.sin(x)
        elif function=="2":
            y=x**2
        elif function=="3":
            y=np.sqrt(x)
        else:
            print("Неверный ввод")
            welcome()
    get_diff_table(x,y)
    boolean=True
    while(boolean):
        method = getMethod()
        arg=getArgument()
        if arg<x[0] or arg>x[-1]:
            print("ВНМИАНИЕ!!!! Аргумент не входит в отрезок интерполяции и результат может быть неверным")
        if(arg-x[len(x)//2]/(x[1]-x[0])>0.75 or arg-x[len(x)//2]/(x[1]-x[0])<-0.75):
            print("ВНМИАНИЕ!!!! Аргумент находится далеко от центра отрезка интерполяции и результат может быть неверным для методов стирлинга и бесселя")
        if(len(x)%2==0):
            print("ВНИМАНИЕ!!!! Результат может быть неверен для метода стирлинга, так как количество точек четное")
        else:
            print("ВНИМАНИЕ!!!! Результат может быть неверен для метода бесселя, так как количество точек нечетное")
        if method==1:
            print("Значение интерполяционного многочлена Лагранжа в точке",arg,"равно",lagrange(x,y)(arg))
            print("Хотите посмотреть график? (y/n)")
            if input()=="y":
                draw_lagrange(x,y)
                draw_points(x,y)
                plt.show()
        elif method==2:
            print("Значение интерполяционного многочлена Ньютона в точке",arg,"равно",newton_method(arg,x,y))
           
            print("Хотите посмотреть график? (y/n)")
            if input()=="y":
                draw_newton(x,y)
                draw_points(x,y)
                plt.show()
        elif method==3:
            print("Значение интерполяционного многочлена Ньютона в форме Стирлинга в точке",arg,"равно",steerling_interpolation(arg,x,y))
            print("Хотите посмотреть график? (y/n)")
            if input()=="y":
                draw_stirling(x,y)
                draw_points(x,y)
                plt.show()
        elif method==4:
            print("Значение интерполяционного многочлена Ньютона в форме Бесселя в точке",arg,"равно",bessel_interpolation(arg,x,y))
            print("Хотите посмотреть график? (y/n)")
            if input()=="y":
                draw_bessel(x,y)
                draw_points(x,y)
                plt.show()
        print("Хотите посмотреть значения в других интерполяциях? (y/n)")
        if input()=="y":
            print("1 - Многочлен Лагранжа")
            print("Значение интерполяционного многочлена Лагранжа в точке",arg,"равно",lagrange(x,y)(arg))
            print("2 - Многочлен Ньютона")
            print("Значение интерполяционного многочлена Ньютона в точке",arg,"равно",newton_method(arg,x,y))
            print("3 - Интерполяционный многочлен Ньютона в форме Стирлинга")
            print("Значение интерполяционного многочлена Ньютона в форме Стирлинга в точке",arg,"равно",steerling_interpolation(arg,x,y))
            print("4 - Интерполяционный многочлен Ньютона в форме Бесселя")
            print("Значение интерполяционного многочлена Ньютона в форме Бесселя в точке",arg,"равно",bessel_interpolation(arg,x,y))
        print("Хотите посмотреть таблицу разделенных разностей? (y/n)")
        if input()=="y":
            get_diff_table(y)
        print("Хотите посмотреть все графики? (y/n)")
        if input()=="y":
            draw_all(x,y)
            plt.show()
        print("Хотите продолжить? (y/n)")
        if input()=="n":
            boolean=False

    

welcome()
