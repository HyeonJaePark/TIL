import java.io.*;
import java.math.BigInteger;

class Main{
    static int Int(String s) {
        return Integer.parseInt(s);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();
        int n = Int(br.readLine());
        BigInteger[] arr = new BigInteger[n];
        for(int i = 0; i < n; i++) {
            arr[i] = new BigInteger(br.readLine(), 2);
        }
        int q = Int(br.readLine());
        for(int i = 0; i < q; i++) {
            String[] line = br.readLine().split(" ");
            sb.append(arr[Int(line[0]) - 1].and(arr[Int(line[1]) - 1]).bitCount() + "\n");
        }
        System.out.println(sb);
    }
}