#include <bits/stdc++.h>
using namespace std;

int n, s;
int arr[21];
int answer = 0;

void func(int x, int t) {
    if (x == n) {
        if (t == s) answer++;
        return;
    }
    func(x + 1, t + arr[x]);
    func(x + 1, t);
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> s;
    for (int i = 0; i < n; i++) cin >> arr[i];
    func(0, 0);
    if (s == 0) answer--;
    cout << answer;
    return 0;
}