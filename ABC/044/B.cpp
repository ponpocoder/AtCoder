#include <iostream>
#include <map>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  string w;
  cin >> w;
  map<char, int> mp;
  for (auto c : w) {
    mp[c] += 1;
  }
  for (auto x: mp) {
    if (x.second % 2 != 0) {
      cout << "No" << endl;
      return 0;
    }
  }
  cout << "Yes" << endl;
}
