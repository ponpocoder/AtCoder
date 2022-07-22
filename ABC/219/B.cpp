#include <iostream>

using namespace std;

int main() {
  string s1, s2, s3, t;
  cin >> s1 >> s2 >> s3 >> t;
  string res = "";

  for(char c : t) {
    if (c == '1') res += s1;
    else if (c == '2') res += s2;
    else res += s3;
  }
    cout << res << endl;
}
