#include <iostream>

using namespace std;

int main(){
    int tamanhos;
    cin >> tamanhos;
    int chinelos[tamanhos];

    for (int i=0; i<tamanhos; i++){
        cin >> chinelos[i];
    }

    int pedidos;
    cin >> pedidos;
    int pedidos_chinelos[pedidos];

    for (int j=0; j<pedidos; j++){
        cin >> pedidos_chinelos[j];
    }

    int quant_pedidos;
    quant_pedidos = 0;
  
    for (int k=0; k<pedidos; k++){
        int solic = (pedidos_chinelos[k])-1;
        if (chinelos[solic] > 0){
            chinelos[solic] = chinelos[solic] - 1;
            quant_pedidos = quant_pedidos + 1;
        }
    }
    cout << quant_pedidos << '\n';
}