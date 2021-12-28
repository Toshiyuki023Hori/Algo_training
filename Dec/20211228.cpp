// https://atcoder.jp/contests/abc051/tasks/abc051_b
#include "bits/stdc++.h"
using namespace std;

int main() {
  // Atcoderの制限は10**6
  // 2500**2でもその制限を満たせるので全探索
  int K, S;
  cin >> K;
  cin >> S;
  int ans = 0;

  for (int i = 0; i <= K; i++) {
    for (int j = 0; j <= K; j++) {
      if (S - i - j <= K && S - i - j >= 0) {
        ans += 1;
      }
    }
  }
  cout << ans << endl;
}
