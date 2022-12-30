#include <iostream>
#include <vector>
#include <map>
#include <set>

using namespace std;
using ll = long long;
using P = pair<int, int>;
#define pb = push_back;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <typename A, typename B>
ostream& operator <<(ostream& out, const pair<A, B>& a) {
  out << "(" << a.first << "," << a.second << ")";
  return out;
}

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  P x;
  x.first = 10;
  x.second = 11;
  cout << x << endl;
}
