function sp = parte1_p4()
  pkg load parallel
  p=q=[1:0.1:25];
  m=241;
  b=ones(m,1);
  A = tridiagonal(p, q, m);
  cantidad_De_Nucleos=nproc
  sp=[];
  tp=[];
  tiempoPara=[];
   tic
    solNpll = parte1_p2(A, b);
    ts=toc
  for i=1:cantidad_De_Nucleos
    tic
    solpll = jacobi_paralelo(A, b, i);
    tpI=toc;
    tiempoPara=[tiempoPara tpI];
    sp=[sp ts/tpI];
  endfor
  tp=tiempoPara

endfunction

function [x_k, k, error] = jacobi_paralelo(A, b,npc)
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
            x_k = (pararrayfun(npc, @(n) parte1_p3(A, b, x_k, m, n), 1:m))';
        endif
    endfor
endfunction