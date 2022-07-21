#define LOCAL
#include <iostream>
#include <vector>

//typedef long long ll;
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> a;
  while (n) {
    a.push_back(n%10);
    n /= 10;
  }
  sort(a.begin(), a.end());
  int k = a.size();
  int ans = 0;
  do {
    for (int i = 1; i <= k-1; i++){
      if (a[0] == 0) continue;
      if (a[i] == 0) continue;
      int l = 0, r = 0;
      for (int j = 0; j < i; j++) {
        l = l*10+a[j];
      }
      for (int j = i; j < k; j++) r = r*10+a[j];
      ans = max(ans, l*r);
    }
  } while (next_permutation(a.begin(), a.end()));
  cout << ans << endl;
}
