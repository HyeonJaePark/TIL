#include <bits/stdc++.h>
using namespace std;

int n;
vector<pair<int, int>> v;
int a, b;
int st = -1'000'000'001;
int en = -1'000'000'001;
int answer;

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> a >> b;
    v.push_back({a, b});
  }
  sort(v.begin(), v.end());
  for (auto i : v) {
    a = i.first;
    b = i.second;
    if (en < a) {
      answer += (en - st);
      st = a;
    }
    if (en < b) en = b;
  }
  answer += (en - st);
  cout << answer;
}