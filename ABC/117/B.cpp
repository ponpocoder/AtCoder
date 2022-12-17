#include <iostream>
#include <vector>
#include <map>
#include <set>

using namespace std;
using ll = long long;
using P = pair<int, int>;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int n;
  cin >> n;
  int mx = 0;
  int s = 0;
  rep(i, n) {
    int l;
    cin >> l;
    chmax(mx, l);
    s += l;
  }
  if(s-mx>mx) cout << "Yes" << endl;
  else cout << "No" << endl;
}
