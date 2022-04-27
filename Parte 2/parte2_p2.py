import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

"""
Newton_Raphson:
    Entrada:
        f: vector de funciones
        x0: vector inicial
        x: vector que contiene las variables
        tol: error mínimo
        iterMax: iteraciones máximas
    Salida:
        xk: vector que aproxima a la solución
        i: cantidad de iteraciones
        error: error
"""
def newton_raphson(f , x0, x, tol, iterMax):
    xk = x0
    errores = []
    J = jacobiano(f, x)
    for i in range(iterMax+1):
        J_eval = eval_jacobiano(J, x, xk)
        f_eval = eval_f(f, x, xk)

        #Resolver sistema de ecuaciones
        y = np.linalg.solve(J_eval, f_eval)

        #Calcular xk
        xk = xk - y
        
        error = np.linalg.norm(eval_f(f, x, xk), 2)
        errores.append(error)
        # print(error)
        if error < tol:
            break
    
    graficar(range(i + 1), errores)
    return xk, i, error

"""
Evalua en f los parametros que recibe
    Entrada: 
        f: vector de funciones
        x: variables por sustituir
        c: vector de preimagenes
    Salida:
        f_eval: vector con las imagenes
"""
def eval_f(f, x, c):
    num_fun = f.size
    num_var = x.size
    c = c[:, 0]
    f = f[:, 0]
    f_eval = np.zeros((num_fun, 1))
    for i in range(num_fun):
        funcion = sp.simplify(f[i])
        for j in range(num_var):
            var = sp.Symbol(x[j])
            funcion = funcion.subs(var, c[j]).evalf()
        f_eval[i] = funcion
    f_eval = f_eval.astype('float64')
    return f_eval

"""
Evalua el parametro de entrada c, en las diferentes derivadas paraciales del jacobiano
    Entrada: 
        J: matriz del jacobiano
        x: variables por sustituir
        c: vector de con los valores que se van a sustituir
    Salida:
        J: Matriz del jacobiano sustituida
"""
def eval_jacobiano(J, x, c):
    m = J.shape[0]
    n = J.shape[1]
    c = c[:, 0]
    for j in range(x.size):
        var = sp.Symbol(x[j])
        for i in range(m):
            for k in range(n):
                J[i, k] = J[i, k].subs(var, c[j]).evalf()
                # print(J[i, k])
    J = J.astype('float64')
    return J

"""
Devuelve el jacobiano
    Entrada:
        f: vector de funciones
        x: vector de variables
    Salida:
        J: Matriz del jacobiano (las derivadas parciales)
"""
def jacobiano(f, x):
    num_fun = f.size
    num_var = x.size
    f = f[:, 0]
    # J = np.zeros((num_var, num_fun), dtype=object)
    J = []
    for i in range(num_var):
        var = sp.Symbol(x[i])
        sub_J = []
        for j in range(num_fun):
            # funcion = sp.sympify(f[j])
            # J[j, i] = sp.diff(funcion, var)
            sub_J.append(sp.diff(f[j], var))
        J.append(sub_J)
    J = np.array(J)
    J = J.transpose()
    return J

"""
Crea un gráfico
Entrada:
    x: iteraciones
    y: errores"""
def graficar(k, errores):
    plt.plot(k, errores)
    plt.xlabel('Iteraciones')
    plt.ylabel('Error')
    plt.show()




