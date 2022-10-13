#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int x;
  cin >> x;
  int n = 1001001;
  vector<bool> prime(n, true);
  for (int i = 2; i < n; i++) {
    if (prime[i]) {
      for (int j = i+i; j < n; j += i) {
        prime[j] = false;
      }
    }
  }
  for (int i = x; i < n; i++) {
    if (prime[i]) {
      cout << i << endl;
      return 0;
    }
  }
}
