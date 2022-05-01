#include "parte3.h"

mat parte_3::pseudo_inversa(const mat& A){
    double tol = 1e-5;
    int iter_max = 1000;

    auto n = A.n_cols;
    mat identidad = eye(n, n);

    int p = 5;
    double norma_k = 0;
    double norma_k_anterior;
    double error;
    mat x_k = (1 / pow(norm(A), 2)) * trans(A);
//    cout << norm(x_k * A - identidad, "fro") << endl;
    int k;
    for(k = 1; k <= iter_max; k++){
//        error = norm(x_k * A - identidad, "fro");
        norma_k_anterior = norma_k;
        norma_k = norm(x_k * A - identidad, "fro");
        error = abs(norma_k - norma_k_anterior);
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
//    cout << k << endl;
    return x_k;
}


using namespace parte_3;
int main() {
    mat A(45, 30);
    for(int i = 0; i < A.n_rows; i++){
        for(int j = 0; j < A.n_cols; j++){
            A(i, j) = pow(i+1, 2) + pow(j+1, 2);
        }
    }

    cout.precision(15);

    mat p_inv = pseudo_inversa(A);
    mat p_inv_buena = pinv(A);

    p_inv.raw_print(cout);
    cout << "----------------------" << endl;
    p_inv_buena.raw_print(cout);
}