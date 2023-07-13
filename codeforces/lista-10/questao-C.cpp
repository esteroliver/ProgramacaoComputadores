#include <bits/stdc++.h>

using namespace std;

int main(){
    string nome;
    cin >> nome;
    int a, c, g, t, letras;
    letras = nome.size();
    a = 1;
    c = 1;
    g = 1;
    t = 1;

    for (int i=0; i<letras; i++){
        if (nome[i] == 'A' && nome[i] == nome[i+1]){
            a = a + 1;
        }
        else if (nome[i] == 'C' && nome[i] == nome[i+1]){
            c = c + 1;
        }
        else if (nome[i] == 'G' && nome[i] == nome[i+1]){
            g = g + 1;
        }
        else if (nome[i] == 'T' && nome[i] == nome[i+1]){
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