#include <bits/stdc++.h>
using namespace std;

stack<int> s;

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);

  string ss;
  int ans = 0;
  int res = 1;

  cin >> ss;
  for (int i = 0; i < ss.size(); i++) {
    if (ss[i] == '(') {
      res *= 2;
      s.push(ss[i]);
    } 
    else if (ss[i] == '[') {
      res *= 3;
      s.push(ss[i]);
    } 
    else if (ss[i] == ')') {
      if (s.empty() || s.top() != '(') {
        cout << 0;
        return 0;
      }
      if (ss[i - 1] == '(') ans += res;
      s.pop();
      res /= 2;
    } 
    else {
      if (s.empty() || s.top() != '[') {
        cout << 0;
        return 0;
      }
      if (ss[i - 1] == '[') ans += res;
      s.pop();
      res /= 3;
    }
  }
  if (s.empty()) cout << ans;
  else cout << 0;
}