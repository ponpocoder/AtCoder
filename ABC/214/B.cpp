#include <iostream>

using namespace std;

typedef long long ll;
#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int s, t;
  cin >> s >> t;
  int res = 0;
  for(int i = 0; i <= s; i++) {
    for (int j = 0; j <= s; j++) {
      for (int k = 0; k <= s; k++) {
        if (i + j + k <= s && i*j*k <= t) {
          res += 1;
        }
      }
    }
  }
  cout << res << endl;
}
