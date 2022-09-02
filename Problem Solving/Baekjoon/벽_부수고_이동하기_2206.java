import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class 벽_부수고_이동하기_2206 {
    static int n, m;
    static int board[][];
    static int visited[][][];
    static int answer = 1000005;
    static int[] dxs = {-1, 1, 0, 0};
    static int[] dys = {0, 0, -1, 1};

    static class Point {
        int x, y, distance;
        boolean isbreaked;

        public Point(int x, int y, boolean isbreaked, int distance) {
            this.x = x;
            this.y = y;
            this.isbreaked = isbreaked;
            this.distance = distance;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        board = new int[n+2][m+2];
        visited = new int[2][n+2][m+2];
        visited[0][1][1] = 1;
        for (int i = 1; i <= n; i++) {
            String s = br.readLine();
            for (int j = 1; j <= m; j++) {
                board[i][j] = s.charAt(j-1) - '0';
            }
        }

        Deque<Point> deque = new ArrayDeque<>();
        deque.add(new Point(1, 1, false, 1));

        while (!deque.isEmpty()) {
            int next_x, next_y, next_distance;
            Boolean isbreaked;
            Point curr = deque.remove();

            if (curr.x == n && curr.y == m) {
                answer = Math.min(answer, curr.distance);
                continue;
            }

            for (int i = 0; i < 4; i++) {
                next_x = curr.x + dxs[i];
                next_y = curr.y + dys[i];
                isbreaked = curr.isbreaked;
                next_distance = curr.distance + 1;
                if (inbound(next_x, next_y)) {
                    if (!isbreaked && visited[0][next_x][next_y] == 0) { // 벽을 안 부셨을 때
                        if (board[next_x][next_y] == 1) {
                            isbreaked = true;
                        }
                        visited[0][next_x][next_y] = next_distance;
                        deque.add(new Point(next_x, next_y, isbreaked, next_distance));
                    }
                    else if (isbreaked && visited[1][next_x][next_y] == 0){ // 벽을 부셨을 때
                        if (board[next_x][next_y] == 0) {
                            visited[1][next_x][next_y] = next_distance;
                            deque.add(new Point(next_x, next_y, isbreaked, next_distance));
                        }
                    }
                }
            }
        }
        System.out.println(answer == 1000005 ? -1 : answer);
    }

    static boolean inbound(int r, int c) {
        return (1 <= r) && (r <= n) && (1 <= c) && (c <= m) ? true : false;
    }
}