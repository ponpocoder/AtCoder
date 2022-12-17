#include <iostream>
#include <vector>
#include <map>
#include <iomanip>

using namespace std;
using ll = long long;
using P = pair<int, int>;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int t, x;
  cin >> t >> x;
  double res = (double)t / x;
  cout << setprecision(10) << res << endl;
}
