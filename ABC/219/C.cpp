#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
  string x;
  int n;
  cin >> x >> n;
  vector<string> s(n);
  for(int i = 0; i < n; i++) cin >> s[i];

  map<char, char> f, g;
  for (int i = 0; i < 26; i++) f[x[i]] = 'a' + i;
  for (int i = 0; i < 26; i++) g['a' + i] = x[i];
  for (int i = 0; i < n; i++) {
    for (char& c : s[i]) c = f[c];
  }
  sort(s.begin(), s.end());
  for (int i = 0; i < n; i++) {
    for (char& c : s[i]) c = g[c];
  }

  for (int i = 0; i < n; i++) cout << s[i] << endl;
}
