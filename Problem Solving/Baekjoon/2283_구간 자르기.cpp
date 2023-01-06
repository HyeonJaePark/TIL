#include <bits/stdc++.h>
using namespace std;

int n, k;
int vis[1000004];
int a, b;

int main(void) {
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> a >> b;
        vis[a+1]++;
        vis[b+1]--;
    }
    for (int i = 1; i <= 1000000; i++) vis[i] += vis[i-1];

    int left = 0, right = 0;
    int sum = 0;
    while (true) {
        if (sum < k) sum += vis[++right];
        else if (sum > k) sum -= vis[++left];
        else {
            cout << left << ' ' << right;
            return 0;
        }
        if (right == 1000001) break;
    }
    cout << "0 0";
}