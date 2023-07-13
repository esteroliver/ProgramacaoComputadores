#include <bits/stdc++.h>

using namespace std;

int main(){
    string nome;
    cin >> nome;
    int a, c, g, t, letras;
    letras = nome.size();
    a = 0;
    c = 0;
    g = 0;
    t = 0;

    for (int i=0; i<letras; i++){
        if (nome[i] == 'A'){
            a = a + 1;
        }
        else if (nome[i] == 'C'){
            c = c + 1;
        }
        else if (nome[i] == 'G'){
            g = g + 1;
        }
        else if (nome[i] == 'T'){
            t = t + 1;
        }
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