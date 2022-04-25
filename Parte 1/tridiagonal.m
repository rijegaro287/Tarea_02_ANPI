function A=tridiagonal(p,q,m)
  A=zeros(m)
    A(1,1)=2*p(1); 
    A(1,2)=q(1); % Primera fila
    
    A(m,m)= 2*(p(m-1)+q(m)); 
    A(m,m-1)=p(m-1); %Ultima fila
    for i=2:m-1             % Restantes Filas
        A(i,i-1)=p(i-1);
        A(i,i)=2*(p(i-1)+q(i));
        A(i,i+1)=q(i);
    end



end