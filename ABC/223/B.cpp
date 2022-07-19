#include <iostream>
using namespace std;
#define rep(i, n) for (int i = 0; i < (n); i++)

int main(){
  string s;
  cin >> s;
  int n = s.size();
  string mn = s, mx = s;
  rep(i, n){
    mn = min(mn, s);
    mx = max(mx, s);
    s += s[0];
    s.erase(s.begin());
  }

  cout << mn << endl;
  cout << mx << endl;
  return 0;
}
