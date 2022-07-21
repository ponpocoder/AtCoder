#define LOCAL
#include <iostream>
#include <math.h>

using namespace std;

int main() {
  int a, b;
  cin >> a >> b;
  int ret;
  ret = pow(32, a-b);
  cout << ret << endl;
}
