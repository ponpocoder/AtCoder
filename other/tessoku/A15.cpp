#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  rep(i, n) cin >> a[i];

  vector<int> s = a;
  sort(s.begin(), s.end());
  s.erase(unique(s.begin(), s.end()), s.end());

  rep(i, n) {
    auto it = lower_bound(s.begin(), s.end(), a[i]);
    if (i >= 1) cout << " ";
    cout << it-s.begin()+1;
  }
  cout << endl;
}
