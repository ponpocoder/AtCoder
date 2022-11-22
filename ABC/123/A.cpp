#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  vector<int> a(5);
  rep(i, 5) cin >> a[i];
  int k;
  cin >> k;
  for(int i=0; i<5; i++) {
      for (int j=i+1; j<5; j++) {
        if (abs(a[i]-a[j]) > k) {
          cout << ":(" << endl;
          return 0;
        }
      }
    }
  cout << "Yay!" << endl;
}
