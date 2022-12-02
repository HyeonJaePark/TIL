#include <bits/stdc++.h>
using namespace std;

queue<int> q;
int n;

int main() {
    cin >> n;
    int card = 1;
    while (n--) q.push(card++);

    while (q.size() > 1) {
        q.pop();
        q.push(q.front());
        q.pop();
    }

    cout << q.front();

    return 0;
}