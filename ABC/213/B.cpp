#include <iostream>
#include <vector>
#include <map>
using namespace std;

#define rep(i, n) for(int i = 0; i < (n); i++)
int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  map<int ,int> m;
  for (int i = 0; i < n; i++){
    cin >> a[i];
    m[a[i]] = i+1;
  }
  sort(a.begin(), a.end());
  cout << m[a[n-2]] << endl;
}
