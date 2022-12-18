import matplotlib.pyplot as plt

import numpy as np

def plotdf(f, xran=[-5, 5], yran=[-5, 5], grid=[21, 21], color='k'):
    """
    Plot the direction field for an ODE written in the form 
        x' = F(x,y)
        y' = G(x,y)
    
    The functions F,G are defined in the list of strings f.
    
    Input
    -----
    f:    list of strings ["F(X,Y)", "G(X,Y)"
          F,G are functions of X and Y (capitals).
    xran: list [xmin, xmax] (optional)
    yran: list [ymin, ymax] (optional)
    grid: list [npoints_x, npoints_y] (optional)
          Defines the number of points in the x-y grid.
    color: string (optional)
          Color for the vector field (as color defined in matplotlib)
    """
    x = np.linspace(xran[0], xran[1], grid[0])
    y = np.linspace(yran[0], yran[1], grid[1])
    def dX_dt(X, Y, t=0): return map(eval, f)
    
    X , Y  = np.meshgrid(x, y)  # create a grid
    DX, DY = dX_dt(X, Y)        # compute growth rate on the grid
    M = (np.hypot(DX, DY))      # Norm of the growth rate 
    M[ M == 0] = 1.             # Avoid zero division errors 
    DX = DX/M                   # Normalize each arrows
    DY = DY/M  
      
    plt.quiver(X, Y, DX, DY, pivot='mid', color=color)
    plt.xlim(xran), plt.ylim(yran)
    plt.grid('on')
    


plt.figure()

plt.show()




def plot (t,x,y,title):
    plt.plot(t, x, t, y)
    print("Show plot")
    plt.title(title)
    
    plt.show()
    plt.close()
    plt.plot(x,y)
    plt.title(str(title+" phase space"))
    plt.show()
  #  plt.plot(t,x,label="x")
   # plt.plot(t,y,label="y")
   # plt.legend(loc="best")