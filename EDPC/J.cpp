#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

double dp[301][301][301];
int n;

double f(int i, int j, int k) {
  if (dp[i][j][k] != -1) return dp[i][j][k];
  dp[i][j][k] = (double)n/(i+j+k);
  if (i > 0) dp[i][j][k] += f(i-1, j, k) * i / (i+j+k);
  if (j > 0) dp[i][j][k] += f(i+1, j-1, k) * j / (i+j+k);
  if (k > 0) dp[i][j][k] += f(i, j+1, k-1) * k / (i+j+k);
  return dp[i][j][k];
}

int main() {
  cin >> n;
  int one = 0;
  int two = 0;
  int thr = 0;

  rep(i, n) {
    int a;
    cin >> a;
    if (a == 1) one++;
    else if (a == 2) two++;
    else thr++;
  }
  rep(i, 301) rep(j, 301) rep(k, 301) dp[i][j][k] = -1;
  dp[0][0][0] = 0;
  cout << setprecision(10) << f(one, two, thr) << endl;

}
