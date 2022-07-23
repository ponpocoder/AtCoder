#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;
#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n;
  cin >> n;
  vector<int> s(n), t(n);
  rep(i, n) cin >> s[i];
  rep(i, n) cin >> t[i];
  rep(i, n*2) {
    t[(i+1)%n] = min(t[(i+1)%n], t[i%n]+s[i%n]);
  }
  rep(i, n) cout << t[i] << endl;
}
