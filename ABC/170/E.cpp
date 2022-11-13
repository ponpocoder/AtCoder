#include <iostream>
#include <set>
#include <vector>

#define rep(i, n) for (int i = 0; i < n; i++)
using namespace std;

int main() {
  int n, q;
  cin >> n >> q;
  vector<int> a(n), b(n);
  vector<multiset<int>> s(200001);
  multiset<int> mx;

  auto getMax = [&](int i) {
    if (s[i].size() == 0) return -1;
    return *s[i].rbegin();
  };
  auto addYochien = [&](int i) {
    int x = getMax(i);
    if (x == -1) return;
    mx.insert(x);
  };
  auto delYochien = [&](int i) {
    int x = getMax(i);
    if (x == -1) return;
    mx.erase(mx.find(x));
  };

  auto addEnji = [&](int i, int x) {
    delYochien(i);
    s[i].insert(x);
    addYochien(i);
  };

  auto delEnji = [&](int i, int x) {
    delYochien(i);
    s[i].erase(s[i].find(x));
    addYochien(i);
  };


  rep(i, n) {
    cin >> a[i] >> b[i];
    addEnji(b[i], a[i]);
  }

  rep(i, q) {
    int c, d;
    cin >> c >> d;
    c--;
    delEnji(b[c], a[c]);
    b[c] = d;
    addEnji(b[c], a[c]);
    int res = *mx.begin();
    printf("%d\n", res);
  }
}
