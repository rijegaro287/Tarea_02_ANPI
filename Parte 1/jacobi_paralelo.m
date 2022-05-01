function [x_k, k, error] = jacobi_paralelo(A, b)
    tol = 1e-5;
    iter_max = 1000;
    m = length(b);

    x_0 = zeros(m, 1);

    x_k = x_0;
    for k = 1:iter_max;
        error = norm(A * x_k - b);
        if error < tol
            break;
        else
            x_k = (pararrayfun(nproc, @(n) calcular_elemento(A, b, x_k, m, n), 1:m))';
        endif
    endfor
endfunction

% p = 1:0.1:25;
% q = p;
% m = length(p) + 1;

% A = tridiagonal(p, q, m);
% b = ones(m, 1);

% [x_k, k, error] = jacobi_paralelo(A, b);

% A \ b %Calcula la solución con octave