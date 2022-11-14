#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int n, m;
  cin >> n >> m;
  vector<int> s(n+1);
  rep(i, m) {
    int l, r;
    cin >> l >> r;
    s[l-1]++; s[r]--;
  }
  int curr = 0;
  rep(i, n+1) {
    int tmp = s[i];
    s[i] = curr;
    curr += tmp;
  }
  int cnt = 0;
  rep(i, n) if (s[i+1] == m) cnt++;
  cout << cnt << endl;
}
