#include <iostream>
#include <armadillo>
#include "parte3_p1.h"

using namespace parte_3;
int main() {
    mat A(45, 30);
    for(int i = 0; i < A.n_rows; i++){
        for(int j = 0; j < A.n_cols; j++){
            A(i, j) = pow(i+1, 2) + pow(j+1, 2);
        }
    }

//    A = mat({
//        {2,  5,  10},
//        {5,  8,  13},
//        {10, 13, 18}
//    });

    mat p_inv = pseudo_inversa(A);

    cout.precision(15);
    p_inv.raw_print(cout);
}