#include <iostream>
#include <vector>
#include <set>

using namespace std;

typedef long long ll;
#define rep(i, n) for (int i = 0; i < (n); i++)

set<string> st;

void dfs(string curr, string rem) {
  if (rem == "") {
    st.insert(curr);
    return;
  }
  for (int i = 0; i < rem.size(); i++) {
    string ns = rem;
    ns.erase(ns.begin()+i);
    dfs(curr+rem[i], ns);
  }
}

int main() {
  int k;
  string s;
  cin >> s >> k;
  dfs("", s);
  vector<string> res;
  for (string t : st) res.push_back(t);
  cout << res[k-1] << endl;
}
