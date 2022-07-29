#include <iostream>
#include <vector>

using namespace std;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n;
  cin >> n;
  int one = 0;
  int two = 0;
  vector<int> h(n);
  rep(i, n) cin >> h[i];
  two = abs(h[0]-h[1]);

  for (int i = 2; i < n; i++) {
    int tmp = two;
    two = min(one+abs(h[i-2]-h[i]), two+abs(h[i-1]-h[i]));
    one = min(tmp, one+abs(h[i-2]-h[i-1]));
  }
  cout << two << endl;
}
