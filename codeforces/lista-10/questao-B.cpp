#include <iostream>

using namespace std;

int main(){
    int competidores, pontos, vencedores;
    cin >> competidores >> pontos;
    vencedores = 0;
    int pontuacao[competidores];

    for (int i=0; i<competidores; i++){
        int fase1, fase2;
        cin >> fase1 >> fase2;
        pontuacao[i] = fase1 + fase2;
    }

    for (int j=0; j<competidores; j++){
        if (pontuacao[j] >= pontos){
            vencedores = vencedores + 1;
        }
    }
    cout << vencedores << '\n';    
}