import java.io.*;
import java.util.StringTokenizer;

public class 가장_긴_바이토닉_부분수열_11054 {
    static int n;
    static int[] arr;
    static int[]increase;
    static int[] decrease;
    static int answer;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        n = Integer.parseInt(br.readLine());
        arr = new int[n+1];
        increase = new int[n+2];
        decrease = new int[n+2];
        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 1; i <= n; i++)
            arr[i] = Integer.parseInt(st.nextToken());
        // 증가 수열 dp
        for (int i = 1; i <= n; i++) {
            for (int j = i-1; j > 0; j--) {
                if (arr[i] > arr[j])
                    increase[i] = Math.max(increase[i], increase[j] + 1);
            }
            if (increase[i] == 0)
                increase[i] = 1;
        }
        // 감소 수열 dp
        for (int i = n; i > 0; i--) {
            for (int j = i+1; j <= n; j++) {
                if (arr[i] > arr[j])
                    decrease[i] = Math.max(decrease[i], decrease[j] + 1);
            }
            if (decrease[i] == 0)
                decrease[i] = 1;
        }
        //
        answer = 0;
        for (int i = 1; i <= n; i++)
            if (answer < increase[i] + decrease[i])
                answer = increase[i] + decrease[i];
        System.out.println(answer - 1);
    }
}
