import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class _1_로_만들기_2_12852 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        
        int answer;
        int[][] visited = new int[n + 1][2];
        for (int[] row : visited) {
            Arrays.fill(row, 10000001);
        }
        int check = 0;
        int curr = n;
        visited[n][0] = check;
        visited[n][1] = curr;
        
        
        for (int i = n; i > 0; i--) {
            check = visited[i][0] + 1;
            if (i % 3 == 0) {
                if (visited[i / 3][0] > check) {
                    visited[i / 3][0] = check;
                    visited[i / 3][1] = i;
                }
            }
            if (i % 2 == 0) {
                if (visited[i / 2][0] > check) {
                    visited[i / 2][0] = check;
                    visited[i / 2][1] = i;
                }
            }
            if (visited[i - 1][0] > check) {
                visited[i - 1][0] = check;
                visited[i - 1][1] = i;
            }
        }

        // trace
        answer = visited[1][0];
        int[] trace = new int[answer + 1];
        trace[0] = 1;
        int tmp = visited[1][1];
        for (int i = 1; i <= answer; i++) {
            trace[i] = tmp;
            tmp = visited[tmp][1];
        }


        bw.write(answer + "\n");
        for (int i = answer; i >= 0; i--) {
            bw.write(trace[i] + " ");
        } 
        bw.flush();
        bw.close();
    }
}
