#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stack>

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
  string s;
  cin >> s;
  stack<char> st;
  set<char> t;
  for(char c: s) {
    if (c == '(') st.push(c);
    else if (c == ')') {
      int cnt = 1;
      while(cnt != 0) {
        char x = st.top(); st.pop();
        if (x == '(') cnt--;
        else if (x == ')') cnt++;
        else t.erase(x);
      }
    } else {
      if (t.count(c)) {
        cout << "No" << endl;
        return 0;
      } else {st.push(c); t.insert(c);}
    }
  }
  cout << "Yes" << endl;
}
