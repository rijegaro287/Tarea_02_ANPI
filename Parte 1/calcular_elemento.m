function [x_n] = calcular_elemento(A, b, x_k, m, n)
    suma_aux = 0;
    for j = 1:m
        if(j != n)
            suma_aux += A(n, j) * x_k(j);
        endif
    endfor

    x_n = 1 / A(n, n) * (b(n) - suma_aux);
endfunction