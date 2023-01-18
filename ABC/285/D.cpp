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
  vector<string> st;
  map<string, vector<string>> mp;
  rep(i, n) {
    string s, t;
    cin >> s >> t;
    st.push_back(s);
    mp[s].push_back(t);
  }
  set<string> visited;
  set<string> visiting;
  auto f = [&](auto f, string curr) -> bool {
    if (visiting.count(curr)) return true;
    if (visited.count(curr)) return false;
    visiting.insert(curr);
    visited.insert(curr);
    for(string dest: mp[curr]) {
      if (f(f, dest)) return true;
    }
    visiting.erase(curr);
    return false;
  };

  for(string s: st) {
    if (f(f, s)) {cout << "No" << endl; return 0;}
  }
  cout << "Yes" << endl;
}
