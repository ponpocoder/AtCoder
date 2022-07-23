#include <iostream>

using namespace std;

typedef long long ll;
#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  string x;
  cin >> x;
  bool step = true;
  bool same = true;
  for(int i = 1; i < x.size(); i++){
    if(x[i] != x[i-1]) same = false;
    int a = x[i-1] - '0';
    int b = x[i] - '0';
    if ((a+1) % 10 != b) step = false;
  }

  if (same || step) cout << "Weak" << endl;
  else cout << "Strong" << endl;
}
