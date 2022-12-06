#include <bits/stdc++.h>
using namespace std;

int n, m;
int board[10][10];
int answer = 90;
int dep = 0;
vector<pair<int, int>> v;

void func_unfill(int x, int y, int dir) {
  // 원래 상태로 되돌리기
  if (dir == 1) {
    for (int i = x - 1; i > 0; i--) {
        if (board[i][y] == 6) break;
        if (board[i][y] >= 1 && board[i][y] <= 5) continue;
        board[i][y] = 0;
    }
  } else if (dir == 2) {
    for (int i = x + 1; i <= n; i++) {
        if (board[i][y] == 6) break;
        if (board[i][y] >= 1 && board[i][y] <= 5) continue;
        board[i][y] = 0;
    }
  } else if (dir == 3) {
    for (int i = y - 1; i > 0; i--) {
        if (board[x][i] == 6) break;
        if (board[x][i] >= 1 && board[x][i] <= 5) continue;
        board[x][i] = 0;
    }
  } else if (dir == 4) {
    for (int i = y + 1; i <= m; i++) {
        if (board[x][i] == 6) break;
        if (board[x][i] >= 1 && board[x][i] <= 5) continue;
        board[x][i] = 0;
    }
  }
}

void func_fill(int x, int y, int dir) {
  // 해당 방향으로 채우기
  if (dir == 1) {
    for (int i = x - 1; i > 0; i--) {
        if (board[i][y] == 6) break;
        if (board[i][y] >= 1 && board[i][y] <= 5) continue;
        board[i][y] = 9;
    }
  } 
  else if (dir == 2) {
    for (int i = x + 1; i <= n; i++) {
        if (board[i][y] == 6) break;
        if (board[i][y] >= 1 && board[i][y] <= 5) continue;
      board[i][y] = 9;
    }
  } 
  else if (dir == 3) {
    for (int i = y - 1; i > 0; i--) {
        if (board[x][i] == 6) break;
        if (board[x][i] >= 1 && board[x][i] <= 5) continue;
        board[x][i] = 9;
    }
  } 
  else if (dir == 4) {
    for (int i = y + 1; i <= n; i++) {
        if (board[x][i] == 6) break;
        if (board[x][i] >= 1 && board[x][i] <= 5) continue;
        board[x][i] = 9;
    }
  }
}

void dfs() {
    if (dep == v.size()) {
        int tot_blank = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (board[i][j] == 0) {
                    tot_blank++;
                }
            }
        }
        if (tot_blank < answer) {
            answer = tot_blank;
        }
        for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= m; j++) {
                    cout << board[i][j] << ' ';
                }
            cout << '\n';
            }
            cout << '\n';
        return;
    }

    pair<int, int> cctv = v.at(dep);
    int cur_x = cctv.first;
    int cur_y = cctv.second;

    if (board[cur_x][cur_y] == 1) {
        // 1번 카메라
        //
        func_fill(cur_x, cur_y, 1);
        dep++;
        dfs();
        dep--;
        func_unfill(cur_x, cur_y, 1);
        //
        func_fill(cur_x, cur_y, 2);
        dep++;
        dfs();
        dep--;
        func_unfill(cur_x, cur_y, 2);
        //
        func_fill(cur_x, cur_y, 3);
        dep++;
        dfs();
        dep--;
        func_unfill(cur_x, cur_y, 3);
        //
        func_fill(cur_x, cur_y, 4);
        dep++;
        dfs();
        dep--;
        func_unfill(cur_x, cur_y, 4);
    } else if (board[cur_x][cur_y] == 2) {
        // 2번 카메라

        func_fill(cur_x, cur_y, 1);
        func_fill(cur_x, cur_y, 2);
        dep++;
        dfs();
        dep--;
        func_unfill(cur_x, cur_y, 1);
        func_unfill(cur_x, cur_y, 2);

        func_fill(cur_x, cur_y, 3);
        func_fill(cur_x, cur_y, 4);
        dep++;
        dfs();
        dep--;
        func_unfill(cur_x, cur_y, 3);
        func_unfill(cur_x, cur_y, 4);
    } else if (board[cur_x][cur_y] == 3) {
        // 3번 카메라
        func_fill(cur_x, cur_y, 1);
        func_fill(cur_x, cur_y, 4);
        dep++;
        dfs();
        dep--;
        func_unfill(cur_x, cur_y, 1);
        func_unfill(cur_x, cur_y, 4);

        func_fill(cur_x, cur_y, 4);
        func_fill(cur_x, cur_y, 2);
        dep++;
        dfs();
        dep--;
        func_unfill(cur_x, cur_y, 4);
        func_unfill(cur_x, cur_y, 2);

        func_fill(cur_x, cur_y, 2);
        func_fill(cur_x, cur_y, 3);
        dep++;
        dfs();
        dep--;
        func_unfill(cur_x, cur_y, 2);
        func_unfill(cur_x, cur_y, 3);

        func_fill(cur_x, cur_y, 3);
        func_fill(cur_x, cur_y, 1);
        dep++;
        dfs();
        dep--;
        func_unfill(cur_x, cur_y, 3);
        func_unfill(cur_x, cur_y, 1);
    } else if (board[cur_x][cur_y] == 4) {
        // 4번 카메라

        func_fill(cur_x, cur_y, 1);
        func_fill(cur_x, cur_y, 4);
        func_fill(cur_x, cur_y, 2);
        dep++;
        dfs();
        dep--;
        func_unfill(cur_x, cur_y, 1);
        func_unfill(cur_x, cur_y, 4);
        func_unfill(cur_x, cur_y, 2);

        func_fill(cur_x, cur_y, 4);
        func_fill(cur_x, cur_y, 2);
        func_fill(cur_x, cur_y, 3);
        dep++;
        dfs();
        dep--;
        func_unfill(cur_x, cur_y, 4);
        func_unfill(cur_x, cur_y, 2);
        func_unfill(cur_x, cur_y, 3);

        func_fill(cur_x, cur_y, 2);
        func_fill(cur_x, cur_y, 3);
        func_fill(cur_x, cur_y, 1);
        dep++;
        dfs();
        dep--;
        func_unfill(cur_x, cur_y, 2);
        func_unfill(cur_x, cur_y, 3);
        func_unfill(cur_x, cur_y, 1);

        func_fill(cur_x, cur_y, 3);
        func_fill(cur_x, cur_y, 1);
        func_fill(cur_x, cur_y, 4);
        dep++;
        dfs();
        dep--;
        func_unfill(cur_x, cur_y, 3);
        func_unfill(cur_x, cur_y, 1);
        func_unfill(cur_x, cur_y, 4);
    } else if (board[cur_x][cur_y] == 5) {
        // 5번 카메라

        func_fill(cur_x, cur_y, 1);
        func_fill(cur_x, cur_y, 4);
        func_fill(cur_x, cur_y, 2);
        func_fill(cur_x, cur_y, 3);
        dep++;
        dfs();
        dep--;
        func_unfill(cur_x, cur_y, 1);
        func_unfill(cur_x, cur_y, 4);
        func_unfill(cur_x, cur_y, 2);
        func_unfill(cur_x, cur_y, 3);
    }
}

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

    dfs();

    cout << answer;
    return 0;
}