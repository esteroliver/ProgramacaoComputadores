#include <iostream>

using namespace std;

int main() {
  int a, b;
  cin >> a >> b;

  int sa[a], sb[b];

  for (int i = 0; i < a; i++) {
    cin >> sa[i];
  }

  for (int l = 0; l < b; l++) {
    cin >> sb[l];
  }

  int seq = 0;
  int j = 0;
  if (b <= a) {
    for (int k = 0; k < a; ++k) {
      if (sa[k] == sb[j]) {
        seq = seq + 1;
        j = j + 1;
      }
    }
    if (seq == b) {
      cout << "S" << '\n';
    } else {
      cout << "N" << '\n';
    }
  }
}
