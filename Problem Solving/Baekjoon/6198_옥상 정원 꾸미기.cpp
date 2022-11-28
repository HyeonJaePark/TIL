#include <bits/stdc++.h>
using namespace std;

stack<int> s;
int n;
long long answer = 0;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    long long h;
    for (int i = 0; i < n; i++) {
        cin >> h;
        while (!s.empty() && s.top() <= h) {
             s.pop();
        }
        answer += s.size();
        s.push(h);
    }

    cout << answer;
    return 0;
}