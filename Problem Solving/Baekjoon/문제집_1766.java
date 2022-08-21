import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;


public class 문제집_1766 {
    static int n, m;
    static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    static int[] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        visited = new int[n + 1];
        
        for (int i = 0; i < n + 1; i++) {
            graph.add(new ArrayList<Integer>());
        }
        
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int q1 = Integer.parseInt(st.nextToken());
            int q2 = Integer.parseInt(st.nextToken());
            graph.get(q1).add(q2);
            visited[q2]++;
        }

        for (int i = 0; i <= n; i++) {
            Collections.sort(graph.get(i));
        }

        topologicalSort();
    }
    public static void topologicalSort() {
        StringBuilder sb = new StringBuilder();
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int i = 1; i < n + 1; i++) {
            if (visited[i] == 0)    pq.add(i);
        }

        while (!pq.isEmpty()) {
            int cur = pq.remove();

            sb.append(cur + " ");

            for (int nextV : graph.get(cur)) {
                visited[nextV]--;
                if (visited[nextV] == 0) pq.add(nextV);
            }
        }

        System.out.println(sb);
    }
}
