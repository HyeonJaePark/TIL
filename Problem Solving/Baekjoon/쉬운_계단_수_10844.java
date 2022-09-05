import java.util.Scanner;

public class 쉬운_계단_수_10844 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        long answer = 0;
        long[][] dp = new long[n][10];
        dp[0] = new long[]{0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0};

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < 10; j++) {
                if (j == 0) {
                    dp[i][j] = dp[i - 1][1] % 1000000000;
                }
                else if (j == 9) {
                    dp[i][j] = dp[i - 1][8] % 1000000000;
                }
                else {
                    dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % 1000000000;
                }
            }
        }

        for (int i = 0; i < 10; i++) {
            answer += dp[n - 1][i];
        }
        System.out.println(answer % 1000000000);

        sc.close();
    }
}
