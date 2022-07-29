#include <iostream>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n;
  cin >> n;
  int day = 0;
  int total = 0;
  while (total < n) {
    day++;
    total += day;
  }
  cout << day << endl;
}
