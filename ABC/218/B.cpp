#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n = 26;
  vector<int> p(n);
  for (int i = 0; i < n; i++) cin >> p[i];

  string res = "";
  for (int i = 0; i < n; i++) res += 'a' + (p[i] - 1);
  cout << res << endl;
}
