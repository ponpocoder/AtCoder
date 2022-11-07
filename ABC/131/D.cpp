#include <iostream>
#include <vector>

using namespace std;

#define rep(i, n) for (int i = 0; i < n; i++)
using P = pair<int, int>;
using ll = long long;

int main() {
  int n;
  cin >> n;
  vector<P> p(n);
  rep(i, n) cin >> p[i].second >> p[i].first;
  sort(p.begin(), p.end());
  ll curr = 0;

  rep(i, n) {
    curr += p[i].second;
    if (curr > p[i].first) {
      cout << "No" << endl;
      return 0;
    }
  }
  cout << "Yes" << endl;
}
