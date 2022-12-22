import numpy as np


def runge_kutta_system(f, g, x0, y0, a, b, h):
    """_summary_
    Args:
        f (funt func): evaluar la funcion f
        g (funt func): evaluar la funcion g
        x0 ( float): valor inicial de x
        y0 (float): valor inicial de y
        a (float): paso de partida
        b (float): paso de llegada
        h (float): tamaño del paso

    Returns:
        tupple t,x,y: t=array con valor de pasos
                        x=array con valor de x
                        y=array con valor de y
    """
    t = np.arange(a, b + h, h)
    n = len(t)
    x = np.zeros(n)
    y = np.zeros(n)
    x[0] = x0
    y[0] = y0
    for i in range(n - 1):
        k1 = h * f(x[i], y[i], t[i])
        l1 = h * g(x[i], y[i], t[i])
        k2 = h * f(x[i] + (k1 / 2), y[i] + (l1 / 2), t[i] + (h / 2))
        l2 = h * g(x[i] + (k1 / 2), y[i] + (l1 / 2), t[i] + (h / 2))
        k3 = h * f(x[i] + (k2 / 2), y[i] + (l2 / 2), t[i] + (h / 2))
        l3 = h * g(x[i] + (k2 / 2), y[i] + (l2 / 2), t[i] + (h / 2))
        k4 = h * f(x[i] + k3, y[i] + l3, t[i] + h)
        l4 = h * g(x[i] + k3, y[i] + l3, t[i] + h)
        x[i + 1] = x[i] + (1 / 6) * (k1 + (2 * k2) + (2 * k3) + k4)
        y[i + 1] = y[i] + (1 / 6) * (l1 + (2 * l2) + (2 * l3) + l4)

    return t, x, y


def Euler_Mod(f, g, x0, y0, a, b, h):

    t = np.arange(a, b+h, h)
    n = len(t)
    x = np.zeros(n)
    y = np.zeros(n)
    x[0] = x0
    y[0] = y0
    for i in range(n - 1):
        k1 = h * f(x[i], y[i], t[i])
        l1 = h * g(x[i], y[i], t[i])
        k2 = h * f(x[i]+k1, y[i]+l1, t[i]+(h/2))
        l2 = h * g(x[i]+k1, y[i]+l1, t[i]+(h/2))
        x[i+1] = x[i]+((1/2)*(k1+k2))
        y[i+1] = y[i]+((1/2)*(l1+l2))

    return t, x, y
