function [x_k, k, error] = parte1_p2(A, b)
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
            for i = 1:m
                suma_aux = 0;
                for j = 1:m
                    if(j != i)
                        suma_aux += A(i, j) * x_k(j);
                    endif
                endfor
            
                x_k(i) = 1 / A(i, i) * (b(i) - suma_aux);
            endfor
        endif
    endfor
endfunction

% p = 1:0.1:25;
% q = p;
% m = length(p) + 1;

% A = tridiagonal(p, q, m);
% b = ones(m, 1);

% [x_k, k, error] = parte1_p2(A, b);