#include <bits/stdc++.h>
using namespace std;

int n;
int answer[40001];

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> n;
  int temp;
  int idx = 0;
  for (int i = 1; i <= n; i++) {
    cin >> temp;
    if (idx == 0)
      answer[idx++] = temp;
    else {
      if (answer[idx - 1] < temp)
        answer[idx++] = temp;
      else
        answer[lower_bound(answer, answer + idx, temp) - answer] = temp;
    }
  }
  cout << idx;
}
