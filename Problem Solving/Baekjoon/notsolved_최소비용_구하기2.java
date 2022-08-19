import java.io.*;
import java.util.*;

public class notsolved_최소비용_구하기2 {
    static HashMap<Integer, HashMap<Integer, Integer>> costs = new HashMap<>();
    static int n, m;

    public static HashMap<Integer, Integer> getMap(int dest, int cost){
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(dest, cost);
        return map;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        int s, d, c;
        for (int i = 0; i < m; i++) {
            s = Integer.parseInt(st.nextToken());
            d = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            costs.put(s, getMap(d, c));
        }
        
    }
}
