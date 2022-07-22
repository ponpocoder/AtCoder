#include <iostream>

using namespace std;

typedef long long ll;
#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  ll n;
  cin >> n;
  string s;
  while (n) {
    if(n%2) {
      n--;
      s += "A";
    } else {
      n /= 2;
      s += "B";
    }
  }

  reverse(s.begin(), s.end());
  cout << s << endl;
}
