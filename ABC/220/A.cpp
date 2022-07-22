#define LOCAL
#include <iostream>

using namespace std;

int main() {
  int a, b, c;
  cin >> a >> b >> c;
  for(int i = 1; i <= c; i++){
    if (c * i >= a and c * i <= b) {
      cout << c * i << endl;
      return 0;
    }
  }
    cout << -1 << endl;
}
