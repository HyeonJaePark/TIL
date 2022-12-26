#include <bits/stdc++.h>
using namespace std;

int dp[100005];
int answer = -987654321;

int main(void) {
  int n;
  cin >> n;

  int sum = 0;
  for (int i = 0; i < n; i++) {
    int a;
    cin >> a;
    if (a > sum + a) {
      dp[i] = a;
      sum = a;
    } else {
      sum += a;
      dp[i] = sum;
    }
    if (dp[i] > answer) answer = dp[i];
  }
  cout << answer;
}