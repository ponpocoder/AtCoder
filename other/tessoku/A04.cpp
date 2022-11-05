#include <iostream>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n;
  cin >> n;

  for (int i = 9; i >= 0; i--) {
    int x = 1 << i;
    cout << (n / x) % 2;
  }
  cout << endl;
}
