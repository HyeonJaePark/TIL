#include <bits/stdc++.h>
using namespace std;

int board[21][21];
int n;
int answer = 2;

void dfs(int dep);

void findMax() {
  int tmpMax = 0;
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
      if (board[i][j] > tmpMax) tmpMax = board[i][j];
    }
  }

  if (tmpMax > answer) answer = tmpMax;
}

void left(int dep) {
  int tmp[21][21];
  memcpy(tmp, board, sizeof(board));

  for (int i = 1; i <= n; i++) {
    deque<int> d;
    int j = 1;
    int p = -1;
    while (j <= n) {
      if (board[i][j] > 0 && board[i][j] == p) {
        d.push_back(p * 2);
        p = -1;
      } else if (board[i][j] > 0 && board[i][j] != p) {
        if (p > 0) d.push_back(p);
        p = board[i][j];
      }
      j++;
    }
    if (p > 0) d.push_back(p);

    for (j = 1; j <= n; j++) {
      if (d.size() > 0) {
        board[i][j] = d[0];
        d.pop_front();
      } else
        board[i][j] = 0;
    }
  }

  dfs(dep + 1);
  memcpy(board, tmp, sizeof(tmp));
}

void right(int dep) {
  int tmp[21][21];
  memcpy(tmp, board, sizeof(board));

  for (int i = 1; i <= n; i++) {
    deque<int> d;
    int j = n;
    int p = -1;
    while (j > 0) {
      if (board[i][j] > 0 && board[i][j] == p) {
        d.push_back(p * 2);
        p = -1;
      } else if (board[i][j] > 0 && board[i][j] != p) {
        if (p > 0) d.push_back(p);
        p = board[i][j];
      }
      j--;
    }
    if (p > 0) d.push_back(p);

    for (j = n; j > 0; j--) {
      if (d.size() > 0) {
        board[i][j] = d[0];
        d.pop_front();
      } else
        board[i][j] = 0;
    }
  }

  dfs(dep + 1);
  memcpy(board, tmp, sizeof(tmp));
}

void up(int dep) {
  int tmp[21][21];
  memcpy(tmp, board, sizeof(board));

  for (int i = 1; i <= n; i++) {
    deque<int> d;
    int j = 1;
    int p = -1;
    while (j <= n) {
      if (board[j][i] > 0 && board[j][i] == p) {
        d.push_back(p * 2);
        p = -1;
      } else if (board[j][i] > 0 && board[j][i] != p) {
        if (p > 0) d.push_back(p);
        p = board[j][i];
      }
      j++;
    }
    if (p > 0) d.push_back(p);

    for (j = 1; j <= n; j++) {
      if (d.size() > 0) {
        board[j][i] = d[0];
        d.pop_front();
      } else
        board[j][i] = 0;
    }
  }

  dfs(dep + 1);
  memcpy(board, tmp, sizeof(tmp));
}

void down(int dep) {
  int tmp[21][21];
  memcpy(tmp, board, sizeof(board));

  for (int i = 1; i <= n; i++) {
    deque<int> d;
    int j = n;
    int p = -1;
    while (j > 0) {
      if (board[j][i] > 0 && board[j][i] == p) {
        d.push_back(p * 2);
        p = -1;
      } else if (board[j][i] > 0 && board[j][i] != p) {
        if (p > 0) d.push_back(p);
        p = board[j][i];
      }
      j--;
    }
    if (p > 0) d.push_back(p);

    for (j = n; j > 0; j--) {
      if (d.size() > 0) {
        board[j][i] = d[0];
        d.pop_front();
      } else
        board[j][i] = 0;
    }
  }

  dfs(dep + 1);
  memcpy(board, tmp, sizeof(tmp));
}

void dfs(int dep) {
  if (dep == 5) {
    findMax();
    return;
  }
  up(dep);
  down(dep);
  right(dep);
  left(dep);
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> n;
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
      int a;
      cin >> a;
      board[i][j] = a;
    }
  }

  dfs(0);

  cout << answer;

  return 0;
}