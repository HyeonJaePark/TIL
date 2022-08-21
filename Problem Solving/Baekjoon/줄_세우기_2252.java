import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 줄_세우기_2252 {
    static int n, m;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        int[] visited = new int[n + 1];

        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n + 1; i++) {
            graph.add(new ArrayList<Integer>());
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s1 = Integer.parseInt(st.nextToken());
            int s2 = Integer.parseInt(st.nextToken());
            graph.get(s1).add(s2);
            visited[s2]++;
        }

        topologicalSort(graph, visited);
    }

    public static void topologicalSort(ArrayList<ArrayList<Integer>> graph, int[] visited) {
        StringBuilder sb = new StringBuilder();
        Queue<Integer> queue = new LinkedList<>();

        for (int i = 1; i <= n; i++) {
            if (visited[i] == 0)    queue.add(i);
        }

        for (int i = 0; i < n; i++) {
            int v = queue.remove();
            sb.append(v + " ");

            for (int nextV : graph.get(v)) {
                visited[nextV]--;

                if (visited[nextV] == 0)    queue.add(nextV);
            }
        }

        System.out.println(sb);
    }
}
