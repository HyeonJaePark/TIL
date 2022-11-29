#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, l;
    deque<pair<int, int>> d;
    cin >> n >> l;
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;

        while (!d.empty() && d.back().second >= a) {
            d.pop_back();
        }
        

        d.push_back({i, a});

        if (d.front().first < i - l + 1) {
            d.pop_front();
        }

        cout << d.front().second << " ";
    }

    return 0;
}
