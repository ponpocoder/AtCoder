#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  rep(i, n) cin >> a[i];
  for(int i=n-1; i > 0; i--) {
    vector<int> x(n);
    if (i%2) {
      rep(j, i) x[j] = max(a[j], a[j+1]);
    } else {
      rep(j, i) x[j] = min(a[j], a[j+1]);
    }
    swap(a, x);
  }
  cout << a[0] << endl;
}
