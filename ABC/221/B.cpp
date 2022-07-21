#define LOCAL
#include <iostream>

using namespace std;

int main() {
  string s, t;
  cin >> s >> t;
  int n = s.size();
  bool ok = false;
  if (s == t) ok = true;
  for(int i = 1; i < n; i++){
    string ns = s;
    swap(ns[i], ns[i-1]);
    if(ns == t) ok = true;
  }
  if (ok) cout << "Yes" << endl;
  else cout << "No" << endl;
}
