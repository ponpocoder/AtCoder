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

struct DS {
  int k;
  ll sum;
  multiset<int> a, b;
  DS(int k): k(k), sum(0) {}
  void ladd(int x) {
    sum += x;
    a.insert(x);
  }
  void lerase(multiset<int>::iterator it) {
    sum -= *it;
    a.erase(it);
  }
  void add(int x) {
    ladd(x);
    if(a.size() <= k) return;
    auto it = a.end(); it--;
    b.insert(*it);
    lerase(it);
  }
  void erase(int x) {
    if(*a.rbegin() < x) {
      b.erase(b.find(x));
    } else {
      lerase(a.find(x));
      auto it = b.begin();
      ladd(*it);
      b.erase(it);
    }
  }
};

int main() {
  int n, m, k;
  cin >> n >> m >> k;
  vector<int> a(n);
  rep(i, n) cin >> a[i];
  DS ds(k);
  rep(i, m) ds.add(a[i]);
  cout << ds.sum << endl;
  rep(i, n-m) {
    ds.add(a[i+m]);
    ds.erase(a[i]);
    cout << ds.sum << endl;
  }
}
