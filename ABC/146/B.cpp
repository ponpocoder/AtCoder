#include <iostream>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n;
  cin >> n;
  string s;
  cin >> s;
  rep(i, s.size()) {
    s[i] = (s[i] - 'A' + n) % 26 + 'A';
  }
  cout << s << endl;
}
