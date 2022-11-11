#include <iostream>
#include <vector>

using namespace std;
using ll = long long;
using P = pair<string, int>;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n;
  cin >> n;
  vector<tuple<string, int, int>> a;
  rep(i, n) {
    string s;
    int p;
    cin >> s >> p;
    a.push_back(make_tuple(s, -p, i));
  }
  sort(a.begin(), a.end());
  rep(i, n) cout << get<2>(a[i])+1 << endl;
}
