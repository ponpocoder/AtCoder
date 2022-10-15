#include <iostream>

using namespace std;

int main() {
  int n;
  string s;
  cin >> n;
  cin >> s;
  if (n % 2) {
    cout << "No" << endl;
    return 0;
  }
  string t = s.substr(0, n/2);
  string u = s.substr(n/2, n);
  if (t == u) cout << "Yes" << endl;
  else cout << "No" <<endl;
}
