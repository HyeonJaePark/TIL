import java.io.*;

public class notsolved_LCS_9251{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] a = br.readLine().toCharArray();
        char[] b = br.readLine().toCharArray();
        int[][] lcs = new int[a.length + 1][b.length + 1];
        int answer = 0;
        for (int i = 1; i <= a.length; i++) {
            for (int j = 1; j <= b.length; j++) {
                if (a[i-1] == b[j-1])
                    lcs[i][j] = lcs[i-1][j-1] + 1;
                else
                    lcs[i][j] = Math.max(lcs[i-1][j], lcs[i][j-1]);
                if (answer < lcs[i][j])
                    answer = lcs[i][j];
            }
        }
        System.out.println(answer);
    }
}