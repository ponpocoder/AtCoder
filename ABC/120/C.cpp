#include <iostream>
#include <vector>
#include <map>
#include <set>

using namespace std;
using ll = long long;
using P = pair<int, int>;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  string s;
  cin >> s;
  vector<char> a;
  int cnt = 0;
  for(auto c: s) {
    if (c == '0' && a.size() && a[a.size()-1] == '1') {
      a.pop_back();
      cnt+=2;
    } else if (c == '1' && a.size() && a[a.size()-1] == '0') {
      a.pop_back();
      cnt+=2;
    } else a.push_back(c);
  }
  cout << cnt << endl;
}
