#include <bits/stdc++.h>
using namespace std;

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int n, s;
  int arr[21];
  int answer = 0;

  cin >> n >> s;
  for (int i = 0; i < n; i++) cin >> arr[i];

  for (int i = 0; i < n; i++) {
    vector<int> v;
    for (int j = 0; j < i; j++) v.push_back(0);
    for (int j = i; j < n; j++) v.push_back(1);
    do {
      int tot = 0;
      for (int j = 0; j < v.size(); j++) {
        if (v.at(j) == 1) tot += arr[j];
      }
      if (tot == s) answer++;
    } while (next_permutation(v.begin(), v.end()));
  }

  cout << answer;
  return 0;
}