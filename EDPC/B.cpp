#include <iostream>
#include <vector>

using namespace std;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n, k;
  cin >> n >> k;
  vector<int> h(n);
  rep(i, n) cin >> h[i];
  const int INF = 1001001001;
  vector<int> cost(n, INF);
  cost[0] = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 1; j <= k; j++) {
      if (i + j > n - 1) break;
      cost[i+j] = min(cost[i+j], cost[i] + abs(h[i]-h[i+j]));
    }
  }
  cout << cost[n-1] << endl;
}
