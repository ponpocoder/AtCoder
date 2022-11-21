#include <iostream>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  string s;
  cin >> s;
  int a = (s[0]-'0')*10+s[1]-'0';
  int b = (s[2]-'0')*10+s[3]-'0';
  if (1<=b && b<=12) {
    if (1<=a && a<=12) cout << "AMBIGUOUS" << endl;
    else cout << "YYMM" << endl;
  } else {
    if (1<=a && a<=12) cout << "MMYY" << endl;
    else cout << "NA" << endl;
  }
}
