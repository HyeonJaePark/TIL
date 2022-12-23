#include <bits/stdc++.h>
using namespace std;

int n, m;
int a[1000005], b[1000005];
int pa, pb;

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> n >> m;
  for (int i = 0; i < n; i++) cin >> a[i];
  for (int i = 0; i < m; i++) cin >> b[i];
  for (int i = 0; i < n + m; i++) {
    if (pa == n)
      cout << b[pb++] << ' ';
    else if (pb == m)
      cout << a[pa++] << ' ';
    else if (a[pa] >= b[pb])
      cout << b[pb++] << ' ';
    else if (a[pa] < b[pb])
      cout << a[pa++] << ' ';
  }
}