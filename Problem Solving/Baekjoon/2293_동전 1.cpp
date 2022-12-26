#include <bits/stdc++.h>
using namespace std;

int n, k;
int dp[10005] = {1};
vector<int> v;

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> n >> k;
  for (int i = 0; i < n; i++) {
    int a;
    cin >> a;
    v.push_back(a);
  }

  for (int i = 0; i < n; i++) {
    for (int j = v.at(i); j <= k; j++) {
      dp[j] += dp[j - v.at(i)];
    }
  }

  cout << dp[k];
}