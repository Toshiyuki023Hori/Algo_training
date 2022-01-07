// https://atcoder.jp/contests/abc175/tasks/abc175_b
#include "bits/stdc++.h"
using namespace std;

int main() {
  int N;
  cin >> N;
  vector<int> nums_array(N);
  for (int i = 0; i < N; i++) {
    cin >> nums_array[i];
  }
  cout << N << endl;
  for (int i = 0; i < N; i++) {
    cout << nums_array[i] << endl;
  }
}
