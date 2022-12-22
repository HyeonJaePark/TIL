#include <bits/stdc++.h>
using namespace std;

int n, m;
int board[10][10];
int answer = 90;
int dep = 0;
vector<pair<int, int>> v;

void checkUp(int x, int y) { ; }

void checkRight(int x, int y) { ; }

void checkDown(int x, int y) { ; }

void checkLeft(int x, int y) { ; }

void uncheckUp(int x, int y) { ; }

void uncheckRight(int x, int y) { ; }

void uncheckDown(int x, int y) { ; }

void uncheckLeft(int x, int y) { ; }

int countBlank() { ; }

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> n >> m;
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= m; j++) {
      int a;
      cin >> a;
      board[i][j] = a;
      if (a >= 1 && a <= 5) v.push_back({i, j});
    }
  }

  cout << answer;
  return 0;
}