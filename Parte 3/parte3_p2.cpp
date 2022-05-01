#include "parte3.h"
#include <vector>

using namespace parte_3;
mat parte3_p2(mat B, mat d) {
    /**
	Método para resolver problema propuesto por medio del método de pseudoinversa
	redistribuida.
	Entradas:
	    B: Matriz de efectividad de control
	    d: vector de variables controladas
	Salida:
	    delta: vector de control
	**/

    // Valores iniciales
    mat Bred = B;
    mat c = {{0},{0},{0},{0}};
    mat cp = {{0},{0},{0},{0}};

    for (int i=0; i<1000; i++){
        cp = c;
        mat delta = -c + pseudo_inversa(Bred) * (d + (B * c));

        for(int k = 0; k<delta.size(); k++){  // Se revisa si se satura algun valor
            if (delta(k) < -0.75){
                c(k) = 0.75;
            for (int m = 0; Bred.size(); m++){
                Bred(m,k) = 0;
            }
            }
            if (delta(k) > 0.75){
                c(k) = -0.75;
            for (int m = 0; Bred.size(); m++){
                Bred(m,k) = 0;
            }
            }
        }
        if (cp == c){break;} // Si ningún valor se satura se detiene la iteración
    }

    cout << delta << endl;
    return delta;
}


int main() {
    mat A={{2,-2,-2,-1},{1,1,-3,-2},{2,-2,-1,-1}};
    mat B={0.5,1,1};
    B = B.t();
    parte3_p2(A, B);

    return 0;
}
