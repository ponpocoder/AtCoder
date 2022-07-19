#include <iostream>
using namespace std;

int main() {
  string n;
  cin >> n;
  while(n.size() != 4){
    n = '0' + n;
  }

  cout << n << endl;
}
