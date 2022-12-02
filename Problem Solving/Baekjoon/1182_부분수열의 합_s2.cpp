#include <bits/stdc++.h>
using namespace std;

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int n, s;
  int arr[21];
  int com[21] = {
      0,
  };

  cin >> n >> s;
  for (int i = 0; i < n; i++) cin >> arr[i];

  do {
    for (int j = 0; j < n; j++) {
      if (com[j] == 0) {
        cout << j + 1 << ' ';
      }
    }
    cout << '\n';
  } while (next_permutation(com, com + n));
  return 0;
}