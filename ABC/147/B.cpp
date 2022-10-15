#include <iostream>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  string s;
  cin >> s;
  int n = s.size();
  int cnt = 0;
  for (int i= 0; i < n/2; i++) {
    if(s[i] != s[n-1-i]) cnt++;
  }
  cout << cnt << endl;
}
