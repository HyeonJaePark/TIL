#include <bits/stdc++.h>
using namespace std;

#define X first
#define Y second

int board[502][502];
bool visited[502][502];
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    int art_cnt = 0, art_size = 0;

    cin >> n >> m;

    for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                int a;
                cin >> a;
                board[i][j] = a;
            }
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (visited[i][j] || board[i][j] == 0) continue;
            queue<pair<int, int>> q;
            q.push({i, j});
            visited[i][j] = true;
            int cur_size = 1;
            art_cnt += 1;
            while (!q.empty()) {
                pair<int, int> cur = q.front(); q.pop();
                for (int k = 0; k < 4; k++) {
                    int nx = cur.X + dx[k];
                    int ny = cur.Y + dy[k];
                    if (nx < 1 || nx > n || ny < 1 || ny > m) continue;
                    if (visited[nx][ny] || board[nx][ny] != 1) continue;
                    visited[nx][ny] = true;
                    q.push({nx, ny});
                    cur_size += 1;
                }
            }
            if (art_size < cur_size) art_size = cur_size;
        }
    }

    cout << art_cnt << '\n' << art_size;
    return 0;
}