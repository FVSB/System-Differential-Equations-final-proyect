import matplotlib.pyplot as plt
from scipy.integrate import odeint
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

    X, Y = np.meshgrid(x, y)  # create a grid
    DX, DY = dX_dt(X, Y)        # compute growth rate on the grid
    M = (np.hypot(DX, DY))      # Norm of the growth rate
    M[M == 0] = 1.             # Avoid zero division errors
    DX = DX/M                   # Normalize each arrows
    DY = DY/M

    plt.quiver(X, Y, DX, DY, pivot='mid', color=color)
    plt.xlim(xran), plt.ylim(yran)
    plt.grid('on')


plt.figure()

plt.show()


def plot(t, x, y, title):
    plt.plot(t, x, t, y)
    print("Show plot")
    plt.title(title)

    plt.show()
    plt.close()
    plt.plot(x, y)
    plt.title(str(title+" phase space"))
    plt.show()
  #  plt.plot(t,x,label="x")
   # plt.plot(t,y,label="y")
   # plt.legend(loc="best")


def Plot_Fields(f, g, t=0):

    y1 = np.linspace(-2.0, 8.0, 20)
    y2 = np.linspace(-2.0, 2.0, 20)

    Y1, Y2 = np.meshgrid(y1, y2)

    u, v = np.zeros(Y1.shape), np.zeros(Y2.shape)

    NI, NJ = Y1.shape

    for i in range(NI):
        for j in range(NJ):
            x = Y1[i, j]
            y = Y2[i, j]

            u[i, j] = f(x, y, t)
            v[i, j] = g(x, y, t)

        Q = plt.quiver(Y1, Y2, u, v, color='r')

        plt.xlabel('$y_1$')
        plt.ylabel('$y_2$')
        plt.xlim([-2, 8])
        plt.ylim([-4, 4])
        
        
        
def Isoclinas(f,points=[0, 0.5, 1, 1.5, 2, 2.5]):
    
    for y20 in points:
        tspan = np.linspace(0, 0.5, 20)
        y0 = [0.0, y20]
        ys = odeint(f, y0, tspan)
        plt.plot(ys[:,0], ys[:,1], 'b-') # path
        plt.plot([ys[0,0]], [ys[0,1]], 'o') # start
        plt.plot([ys[-1,0]], [ys[-1,1]], 's') # end
        

    plt.xlim([-2, 8])

    plt.show()




def fieldplot(f,g,xmin,xmax,ymin,ymax,color='b',aspect=None,nx=20,boostarrows=1.):
    #plt.clf()
    #figure(figsize=(12,12))
    #figure(figsize=(8,8),facecolor='w')
    #nx = 20
    xr = xmax-xmin
    yr = ymax-ymin
    ny = int(nx*yr/xr)
    if aspect!=None:
        plt.subplot(111,aspect=aspect)
    X,Y = np.meshgrid( np.linspace(xmin,xmax,nx), np.linspace(ymin,ymax,ny) )
    X = X.flatten()
    Y = Y.flatten()
    U = f(X,Y)
    V = g(X,Y)
    #print(U)
    #print(V)
    # scale length of arrows - note arrowhead is added beyond the end of the line segment
    h = boostarrows*0.9*min(xr/float(nx-1)/abs(U).max(),yr/float(ny-1)/abs(V).max())
    Xp = X + h*U
    Yp = Y + h*V
    arrowsX = np.vstack((X,Xp))
    arrowsY = np.vstack((Y,Yp))
    head_width  = 0.005*xr
    head_length = head_width/0.6
    for x,y,u,v in zip(X,Y,U,V):
        plt.arrow( x,y, h*u,h*v, fc=color, ec=color, alpha=0.5, width=head_width/5, head_width=head_width, head_length=head_length )
    plt.xlim(xmin,xmax) # plot ranges strangely are [0,1] x [0,1] otherwise
    plt.ylim(ymin,ymax)
    