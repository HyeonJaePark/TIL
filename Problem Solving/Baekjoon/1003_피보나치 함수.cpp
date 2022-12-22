#include <bits/stdc++.h>
using namespace std;

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int dp[42] = {1};
  for (int i = 2; i < 42; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    int n;
    cin >> n;
    cout << dp[n] << ' ' << dp[n + 1] << '\n';
  }
}