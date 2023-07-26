#include <iostream>

using namespace std;

int main(){
    int num;
    while(cin >> num){
        int numeros[num];
            
        for(int i=0; i<num; i++){
            cin >> numeros[i];
        }
        int indice = num-1;
        int sequencia[indice];
            
        for (int j=1;j<num;j++){
            sequencia[j-1] = j;
        }
            
        int seq = 0;

        for (int k=0; k<(num-2);k++){
            for (int l=1; l<num; l++){
                int numero = numeros[l] - numeros[l-1];
                if (numero < 0){
                    numero = numero * -1;
                }
                if (sequencia[k] == numero) seq = seq + 1;
            }
            
        }

        cout << seq << '\n';
        if(seq == num-1 || num == 1){
            cout << "Alegre" << '\n';
        }
        else{
            cout << "Nao alegre" << '\n';
        }
    }
}
