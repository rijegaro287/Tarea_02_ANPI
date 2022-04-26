#include "parte3_p1.h"

mat parte_3::pseudo_inversa(const mat& A){
    cout.precision(10);

    double tol = 1e-5;
    int iter_max = 10;

    auto n = A.n_cols;
    mat identidad = eye(n, n);

    int p = 5;
    double error;
    mat x_k = (1 / pow(norm(A), 2)) * trans(A);

    for(int k = 1; k <= iter_max; k++){
//        error = std::abs(norm(x_k * A - identidad, "fro") - 1);
        error = norm(x_k * A - identidad, "fro");
//        cout << x_k << endl;
//        cout << error << endl;
        if(error < tol){
            break;
        } else{
            mat mult_aux = A * x_k;
            mat suma_aux = zeros(mult_aux.n_rows, mult_aux.n_cols);
            for(int q = 1; q <= p; q++){
                double constante = ((pow(-1, q - 1) * tgamma(p + 1)) / (tgamma(q + 1) * tgamma(p - q + 1)));
                suma_aux += constante * powmat(mult_aux, q - 1);
            }
            x_k = x_k * suma_aux;
        }
    }
    return x_k;
}