import numpy as np
from parte2_p2 import newton_raphson

#* fa
fa = np.array([["exp(x**2) - exp(sqrt(2)*2)"], ["x - y"]])
xa = np.array(["x", "y"])
x0a =  np.array([[2.3], [2.3]])

#* fb
fb = np.array([["x + exp(y) - cos(y)"], ["3*x - y - sin(y)"]])
xb = np.array(["x", "y"])
x0b =  np.array([[1.5], [2]])

#* fc
fc = np.array([["x**2 - 2*x - y + 0.5"], ["x**2 + 4*y**2 - 4"]])
xc = np.array(["x", "y"])
x0c =  np.array([[3], [2]])

#* fd
fd = np.array([["x**2 + y**2 - 1"], ["x**2 - y**2 + 0.5"]])
xd = np.array(["x", "y"])
x0d =  np.array([[0.7], [1.2]])

#* fe
fe = np.array([["sin(x) + y*cos(x)"], ["x - y"]])
xe = np.array(["x", "y"])
x0e =  np.array([[1.2], [-1.5]])

#* fg
fg = np.array([["y*z + w*(y + z)"], ["x*z + w*(x + z)"], ["x*y + w*(x + y)"], ["x*y + x*z + y*z - 1"]])
xg = np.array(["x", "y", "z", "w"])
x0g =  np.array([[-1], [-1], [-1], [-1]])


# resultados = newton_raphson(fa, x0a, xa, 1e-5, 1000)
# resultados = newton_raphson(fb, x0b, xb, 1e-5, 1000)
# resultados = newton_raphson(fc, x0c, xc, 1e-5, 1000)
resultados = newton_raphson(fd, x0d, xd, 1e-5, 1000)
# resultados = newton_raphson(fe, x0e, xe, 1e-5, 1000)
# resultados = newton_raphson(fg, x0g, xg, 1e-5, 1000)
xk = resultados[0]
k = resultados[1]
error = resultados[2]
print(xk)
print(k)
print(error)


