import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 앱_7579 {
    static int n, m;
    static int[] a;
    static int[] c;
    static int[][] dp;
    static int sum;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        a = new int[n+1];
        c = new int[n+1];
        dp = new int[n+1][10001];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++)
            a[i] = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            c[i] = Integer.parseInt(st.nextToken());
            sum += c[i];
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= sum; j++) {
                if (j - c[i] >= 0)
                    dp[i][j] = Math.max(dp[i][j], dp[i - 1][j - c[i]] + a[i]);
                dp[i][j] = Math.max(dp[i][j], dp[i - 1][j]);
            }
        }
        for (int i = 0; i <= sum; i++) {
            if (dp[n][i] >= m) {
                System.out.println(i);
                break;
            }
        }
    }
}