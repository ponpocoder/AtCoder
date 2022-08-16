#include <iostream>
#include <unordered_set>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int k;
  cin >> k;
  int x = 7 % k;
  unordered_set<int> s;
  int cnt = 1;
  while (s.count(x) == 0) {
    if (x == 0) {
      cout << cnt << endl;
      return 0;
    }
    cnt++;
    s.insert(x);
    x = (x*10+7)%k;
  }
  cout << -1 << endl;
}
