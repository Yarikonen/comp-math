import matplotlib.pyplot as plt
import numpy as np
def draw_function(f,a,b):
    x= np.linspace(a,b,1000)
    plt.plot(x,f(x))
    plt.show()