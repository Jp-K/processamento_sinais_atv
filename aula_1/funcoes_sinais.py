import numpy as np
import matplotlib.pyplot as plt
import math

def impulso_unitario(n):
    return 1 if n == 0 else 0

def degrau_unitario(n):
    return 1 if n >= 0 else 0

def gera_impulso_unitario(nMin, nMax, step=1):
    values = []
    for n in np.arange(nMin, nMax, step):
        values.append(impulso_unitario(n))
    
    plt.stem(np.arange(nMin, nMax, step), values, linefmt='r', markerfmt='ro', basefmt='r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Impulso Unitário')
    plt.show()


def gera_degrau_unitario(nMin, nMax, step=1):
    values = []
    for n in np.arange(nMin, nMax, step):
        values.append(degrau_unitario(n))
    
    plt.stem(np.arange(nMin, nMax, step), values, linefmt='r', markerfmt='ro', basefmt='r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Degrau Unitário')
    plt.show()

def gera_sinal_sinusoidal(nMin, nMax, f, fs, mode='cos', step=1):
    values = []
    for n in np.arange(nMin, nMax, step):
        if mode == 'cos':
            values.append(np.cos((2*math.pi*(f/fs))*n))
        else:
            values.append(np.sin((2*math.pi*(f/fs))*n))
    
    plt.plot(np.arange(nMin, nMax, step), values)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Sequência Sinusoidal')
    plt.show()

def gera_sinal_exponencial(nMin, nMax, multiplier, a, step=1):
    values = []
    for n in np.arange(nMin, nMax, step):
        complex_a = np.complex64(a)
        values.append(multiplier*(np.power(complex_a,n)))
    
    plt.plot(np.arange(nMin, nMax, step), values)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Sequência Exponencial')
    plt.show()

if __name__ == "__main__":
    gera_impulso_unitario(-10, 20)

    gera_degrau_unitario(-10, 20)

    gera_sinal_sinusoidal(-100, 200, 100, 8000)
    gera_sinal_sinusoidal(-100, 200, 100, 8000, 'sin')

    gera_sinal_exponencial(0, 30, 1, 0.5, 0.01)
    gera_sinal_exponencial(0, 30, 1, -0.5, 0.01)
    gera_sinal_exponencial(0, 30, 1, 2, 0.01)