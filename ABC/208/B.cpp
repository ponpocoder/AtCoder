#include <iostream>

using namespace std;

int main() {
  int n = 1;
  for(int i = 1; i <= 10; i++) n *= i;
  int res = 0;
  int p;
  cin >> p;

  for (int i = 10; i >= 1; i--) {
    res += p / n;
    p %= n;
    n /= i;
  }
  cout << res << endl;
}
