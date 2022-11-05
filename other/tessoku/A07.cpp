#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int d;
  cin >> d;
  int n;
  cin >> n;
  vector<int> s(d+1);
  rep(i, n) {
    int l, r;
    cin >> l >> r;
    s[l] += 1;
    s[r+1] -= 1;
  }
  int curr = 0;
  for (int i = 1; i <= d; i++) {
    curr += s[i];
    cout << curr << endl;
  }
}
