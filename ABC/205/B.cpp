#include <iostream>
#include <map>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n;
  cin >> n;
  map<int, int> b;
  bool ok = true;
  rep(i, n) {
    int x;
    cin >> x;
    if (x <= 0 || x > n or b[x] == 1) ok = false;
    b[x]++;
  }
  if (ok) cout << "Yes" << endl;
  else cout << "No" << endl;
}
