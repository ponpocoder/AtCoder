#include <iostream>
#include <vector>

using namespace std;

#define rep(i, n) for(int i=0; i < n; i++)

int main() {
  int n = 300001;
  vector<bool> isPrime(n, true);
  isPrime[0] = false;
  isPrime[1] = false;
  rep(i, n) {
    if (!isPrime[i]) continue;
    for(int j = i+i; j <= n; j+=i) {
      isPrime[j] = false;
    }
  }
  int q;
  cin >> q;
  rep(i, q) {
    int x;
    cin >> x;
    if (isPrime[x]) cout << "Yes" << endl;
    else cout << "No" << endl;
  }
}
