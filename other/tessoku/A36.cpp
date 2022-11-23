#include <iostream>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int n, k;
  cin >> n >> k;
  int x = k - (2*n-2);
  if (x>0 && x%2==0) cout << "Yes" << endl;
  else cout << "No" << endl;
}
