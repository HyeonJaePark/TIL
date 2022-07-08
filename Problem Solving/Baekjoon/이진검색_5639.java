import java.io.*;

public class 이진검색_5639 {
    static int[] t = new int[10001];
    static StringBuffer sb = new StringBuffer();
    static void postorder(int start, int end) {
        if (start >= end)
            return;
        if (start == end - 1) {
            sb.append(t[start] + "\n");
            return;
        }
        int i = start + 1;
        while (i < end) {
            if (t[start] < t[i])
                break;
            i++;
        }
        postorder(start + 1, i);
        postorder(i, end);
        sb.append(t[start] + "\n");

        return;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int idx = 0;
        String n;
        while (true) {
            n = br.readLine();
            if (n == null || n == "")
                break;
            t[idx++] = Integer.parseInt(n);
        }
        
        postorder(0, idx);
        System.out.println(sb);
    }
}