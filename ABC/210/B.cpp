#include <iostream>

using namespace std;

typedef long long ll;
#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n;
  cin >> n;
  string s;
  cin >> s;

  int idx = 0;
  for (int i = 0; i < n; i++){
    if (s[i] == '1') {
      idx = i+1;
      break;
    }
  }

  if (idx % 2) cout << "Takahashi" << endl;
  else cout << "Aoki" << endl;
}
