#include <iostream>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int n;
  cin >> n;
  int s = 0;
  rep(i, n) {
    char t;
    int a;
    cin >> t >> a;
    if (t == '+') s += a;
    else if (t == '-') s -= a;
    else s *= a;
    s += 10000;
    s %= 10000;
    cout << s << endl;
  }
}
