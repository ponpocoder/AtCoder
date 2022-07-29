#include <iostream>
#include <vector>

using namespace std;

int main() {
  string s, t;
  cin >> s >> t;
  int a, b;
  a = s.size() + 1;
  b = t.size() + 1;
  vector lcs(a, vector<int>(b, 0));

  for (int i = 1; i < a; i++) {
    for (int j = 1; j < b; j++) {
      if (s[i - 1] == t[j - 1]) lcs[i][j] = lcs[i-1][j-1] + 1;
      else lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1]);
    }
  }

  int i = a-1;
  int j = b-1;
  string res = "";
  while (i > 0 && j > 0) {
    if (lcs[i][j] == lcs[i-1][j]) i--;
    else if (lcs[i][j] == lcs[i][j-1]) j--;
    else {
      res += s[i-1];
      i--;
      j--;
    }
  }
  reverse(res.begin(), res.end());
  cout << res << endl;
}
