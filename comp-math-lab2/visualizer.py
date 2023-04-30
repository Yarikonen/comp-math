import matplotlib.pyplot as plt
import numpy as np
def draw_function(f,a,b):
    plt.clf()
    plt.cla()
    x= np.linspace(a,b,1000)
    plt.plot(x,f(x))
    plt.grid()
def draw_answ(x,y):
    plt.scatter(x,y,color="red")
    plt.show()
def draw_implicit_function(f,a,b):
    plt.clf()
    plt.cla()
    xrange = np.arange(a, b, 0.025)
    yrange = np.arange(a, b, 0.025)
    X,Y = np.meshgrid(xrange,yrange)
    for i in f([X,Y]): plt.contour(X,Y,i,[0])
    plt.grid()
def draw_formula(a):
    plt.plot()
    plt.text(0.5,0.5,'$%s$' %a)
def show():
    plt.show()