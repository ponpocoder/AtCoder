#include <iostream>
#include <vector>

#define rep(i, n) for (int i = 0; i < n; i++)

using namespace std;

void output(int x) {
  vector<int> a;
  int i = 1;
  while (x) {
    if (x&1) a.push_back(i);
    i++;
    x >>= 1;
  }
  cout << a.size();
  for (auto b: a) {
    cout << " " << b;
  }
  cout << endl;
}

int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  rep(i, n) cin >> a[i];
  n = min(n,8);
  vector<int> x(200);
  for (int i = 1; i < (1 << n); i++) {
    int curr = 0;
    rep(j, n) if (i>>j&1) curr = (curr+a[j])%200;
    if (x[curr] == 0) x[curr] = i;
    else {
      cout << "Yes" << endl;
      output(i);
      output(x[curr]);
      return 0;
    }
  }
  cout << "No" << endl;
  return 0;
}
