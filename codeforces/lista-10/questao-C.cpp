#include <bits/stdc++.h>

using namespace std;

int main(){
    string tamanho;
    cin >> tamanho;
    
    char nome[tamanho.size()];

    for (int j=0; j<tamanho.size(); j++){
        nome[j] = tamanho[j];
    }

    int a, c, g, t;
    a = 1;
    c = 1;
    g = 1;
    t = 1;
    
    for (int i=1; i<=tamanho.size(); i++){
        if (nome[i] == 'A' && nome[i-1] != 'A' ) a = 1;
        if (nome[i-1] == 'A' && nome[i] == 'A') a = a + 1;

        if (nome[i] == 'C' && nome[i-1] != 'C') c = 1;
        if (nome[i-1] == 'C' && nome[i] == 'C') c = c + 1;
        
        if (nome[i] == 'G' && nome[i-1] != 'G') g = 1;
        if (nome[i-1] == 'G' && nome[i] == 'G') g = g + 1;

        if (nome[i] == 'T' && nome[i-1] != 'T') t = 1;
        if (nome[i-1] == 'T' && nome[i] == 'T') t = t + 1;
    }

    int repeticoes[] = {a, c, g, t}, maior;
    maior = repeticoes[0];

    for (int j=1; j < 4; j++){
        if (repeticoes[j] > maior){
            maior = repeticoes[j];
        }
    }

    cout << maior << '\n';
}