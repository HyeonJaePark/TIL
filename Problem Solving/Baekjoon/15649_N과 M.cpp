#include <bits/stdc++.h>
using namespace std;

int n, m;
int seq[10];
bool visit[10];

void func(int x) {
    if (x == m) {
        for (int i = 0; i < m; i++) {
            cout << seq[i] << ' ';
        }
        cout << '\n';
        return;
    }
    for (int i = 1; i <= n; i++) {
        if (!visit[i]) {
            seq[x] = i;
            visit[i] = true;
            func(x + 1);
            visit[i] = false;
        }
    }   
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;

    func(0);

    return 0;
}