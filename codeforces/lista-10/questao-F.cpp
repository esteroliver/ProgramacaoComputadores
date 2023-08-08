#include <bits/stdc++.h>

using namespace std;

int main(){
  int num;
  cin >> num;
  int fita[num];

  for (int i=0; i<num; i++){
    cin >> fita[i];
  }

  vector<int> indices;
  int y = 0;
  
  for (int j=0; j<num; j++){
    if (fita[j] == 0){
      indices.push_back(j);
    }
  }
  
  while(y<(indices.size())){
    indices[y] = indices[y+1] - (indices[y]+1);
    if ((y == indices.size() - 1) and indices[y] != 0){
      indices[y] = (indices[y+1] - (indices[y]+1)) - 1;
    }
    y = y+1;
  }

  for(int g=0; g<(indices.size()); g++) cout << indices[g] << '\n';
} 