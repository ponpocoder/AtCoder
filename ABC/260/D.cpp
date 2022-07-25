#include <iostream>
#include <vector>
#include <set>

using namespace std;

typedef long long ll;
#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n, k;
  cin >> n >> k;

  set<int> t;
  vector<int> nxt(n, -1), num(n);
  vector<int> res(n, -1);

  rep(i, n) {
    int p;
    cin >> p;
    p--;
    auto it = t.lower_bound(p);
    if (it == t.end()) {
      num[p] = 1;
    } else {
      int j = *it;
      t.erase(it);
      nxt[p] = j;
      num[p] = num[j] + 1;
    }
    if (num[p] == k) {
      int j = p;
      while (j != -1) {
        res[j] = i + 1;
        j = nxt[j];
      }
    } else {
      t.insert(p);
    }
  }
  rep(i, n) cout << res[i] << endl;
}
