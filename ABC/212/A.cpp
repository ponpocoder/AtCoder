#include <iostream>

using namespace std;

typedef long long ll;
#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int a, b;
  cin >> a >> b;

  if(a > 0 && b ==0) cout << "Gold" << endl;
  else if ( a == 0 && b > 0) cout << "Silver" << endl;
  else cout << "Alloy" << endl;
}
