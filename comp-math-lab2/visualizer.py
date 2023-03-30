import matplotlib.pyplot as plt
import numpy as np
def draw_function(f,a,b):
    x= np.linspace(a,b,1000)
    plt.plot(x,f(x))
    plt.grid()
def draw_answ(x,y):
    plt.scatter(x,y,color="red")
    plt.show()
def draw_implicit_function(f,a,b):
    xrange = np.arange(a, b, 0.025)
    yrange = np.arange(a, b, 0.025)
    X,Y = np.meshgrid(xrange,yrange)
    for i in f([X,Y]): plt.contour(X,Y,i,[0])
