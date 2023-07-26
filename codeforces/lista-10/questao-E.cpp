#include <iostream>

using namespace std;

int main(){
        int num;
        cin >> num;
        int numeros[num];
        
        for(int i=0; i<num; i++){
            cin >> numeros[i];
        }
        
        int sequencia[num-1];
        
        for (int j=1;j<num;j++){
            sequencia[j-1] = (numeros[j] - numeros[j-1]);
            if (sequencia[j-1] < 0) sequencia[j-1] = sequencia[j-1] * -1;
        }
        
        int seq = 1;
        
        for (int k=0; k<(num-1);k++){
            if ((sequencia[k] + 1) == sequencia[k+1] || (sequencia[k] - 1) == sequencia[k+1]){
                seq = seq + 1;
            }
        }
        
        if(seq == num-1 || num == 1){
            cout << "Alegre" << '\n';
        }
        else{
            cout << "Nao alegre" << '\n';
            }
}
