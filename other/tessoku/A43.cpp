#include <iostream>
using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int n, l;
  cin >> n >> l;
  int res = 0;
  rep(i, n) {
    int a;
    char b;
    cin >> a >> b;
    if (b == 'E') res = max(res, l-a);
    else res = max(res, a);
  }
  cout << res << endl;
}
