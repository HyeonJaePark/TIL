#include <bits/stdc++.h>
using namespace std;

int x;
int dp[1000005];

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> x;
    for (int i = 2; i <= x; i++) {
        dp[i] = dp[i - 1] + 1;
        if (i % 3 == 0) dp[i] = min(dp[i / 3] + 1, dp[i]);
        if (i % 2 == 0) dp[i] = min(dp[i / 2] + 1, dp[i]);
    }
    cout << dp[x];
}