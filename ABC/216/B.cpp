#include <iostream>
#include <vector>
#include <set>
using namespace std;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n;
  cin >> n;
  set<string> st;
  rep(i, n) {
    string s, t;
    cin >> s >> t;
    string name = s + " " + t;
    st.insert(name);
  }
  if (st.size() == n) cout << "No" << endl;
  else cout << "Yes" << endl;
}


// int main() {
//   int n;
//   cin >> n;
//   vector<string> s(n), t(n);
//   rep(i, n) cin >> s[i] >> t[i];
//   for (int i = 0; i < n; i++){
//     for (int j = i+1; j < n; j++) {
//       if (s[i] == s[j] && t[i] == t[j]){
//         cout << "Yes" << endl;
//         return 0;
//       }
//     }
//   }
//   cout << "No" << endl;
// }
