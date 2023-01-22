#include <iostream>
#include <vector>
#include <map>
#include <set>

using namespace std;
using ll = long long;
using P = pair<int, int>;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <typename A, typename B>
ostream& operator <<(ostream& out, const pair<A, B>& a) {
  out << "(" << a.first << "," << a.second << ")";
  return out;
}

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int n;
  cin >> n;
  string s;
  cin >> s;
  string res;
  for(int i = 0; i < n;) {
    if (i < n - 1 && s[i] == 'n' && s[i+1] == 'a') {
      res += "nya";
      i += 2;
    } else {
      res.push_back(s[i]);
      i++;
    }
  }
  cout << res << endl;
}
