#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <unordered_set>

using namespace std;
using ll = long long;
using P = pair<int, int>;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  unordered_set<int> s;
  int a;
  cin >> a;
  int cnt = 1;
  while(true) {
    if(s.count(a)) {
      cout << cnt << endl;
      return 0;
    }
    s.insert(a);
    if (a%2) a = 3*a+1;
    else a/= 2;
    cnt++;
  }
}
