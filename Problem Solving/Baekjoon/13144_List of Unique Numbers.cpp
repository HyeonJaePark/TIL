#include <bits/stdc++.h>
using namespace std;

int n;
int arr[100005];
vector<bool> vis(100005);
int answer;

int main(void) {
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> n;
    for (int i = 0; i < n; i++) cin >> arr[i];
    int end = 0;
    vis[arr[0]] = 1;
    for (int start = 0; start < n; start++) {
        while (end < n - 1 && !vis[arr[end + 1]]) {
            end++;
            vis[arr[end]] = 1;
        }
        answer += (end - start + 1);
        vis[arr[start]] = 0;
    }
    cout << answer;
}