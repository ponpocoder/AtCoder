#include <iostream>

using namespace std;

typedef long long ll;
#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  ll n;
  cin >> n;
  int i = 0;
  ll curr = 1;
  while(1) {
    if (curr*2 > n) break;
    curr *= 2;
    i += 1;
  }
  cout << i << endl;
}
