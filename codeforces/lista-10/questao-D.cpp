#include <bits/stdc++.h>

using namespace std;

int main(){
  int num;
  cin >> num;
  int numeros[num];

  for (int i=0; i<num; i++) cin >> numeros[i];

  vector<int> valores;

  for (int j=1; j<num; j++){
    if (numeros[j-1] != numeros[j] && numeros[j+1] != numeros[j]){
      valores.push_back(numeros[j]);
    }
    if (valores[0] == valores[1]) valores.pop_back();
    else if (valores.size() == 2) break;
 }
  
  int seq = 1;
  int k = 0;
  for(int x=1; x<num-1; x++){
    if (k<valores.size()){
      if (numeros[x] == valores[k] && numeros[x-1] != numeros[x] && numeros[x+1] != numeros[x]){
        seq = seq + 1;
        k = k + 1;
      }
    }
    if (x<num) k = 0;
  }

  if(num == 1){
    seq = 1;
  }

  cout << seq << '\n';
}
