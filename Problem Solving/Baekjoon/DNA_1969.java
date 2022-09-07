import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class DNA_1969 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n, m;
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        String[] arr = new String[n];
        for (int i = 0; i < n; i++) {
            arr[i] = br.readLine();
        }
        
        char[] dna = {'A', 'C', 'G', 'T'};
        String answer = "";
        int answer_hd = 0;
        
        for (int i = 0; i < m; i++) {
            int[] f = new int[4];
            for (int j = 0; j < n; j++) {
                switch (arr[j].charAt(i)) {
                    case 'A':
                        f[0]++;
                        break;
                    case 'C':
                        f[1]++;
                        break;
                    case 'G':
                        f[2]++;
                        break;
                    case 'T':
                        f[3]++;
                        break;
                } 
            }
            int idx = 0;
            int tmp = 0;
            for (int j = 0; j < 4; j++) {
                if (f[j] > tmp) {
                    idx = j;
                    tmp = f[j];
                }
            }
            answer_hd += (n - f[idx]);
            answer += dna[idx];
        }
        System.out.println(answer);
        System.out.println(answer_hd);
    }
}