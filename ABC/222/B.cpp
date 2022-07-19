#include <iostream>
using namespace std;

int main() {
  int n, p;
  cin >> n >> p;
  int cnt = 0;
  for(int i = 0; i < n; i++){
    int curr;
    cin >> curr;
    if(curr < p){
      cnt++;
    }
  }
  cout << cnt << endl;
}
