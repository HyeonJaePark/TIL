import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class 과제_13904 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int answer = 0;
        int day = 0;
        PriorityQueue<Pair> pq = new PriorityQueue<Pair>();
        PriorityQueue<Integer> solve = new PriorityQueue<>();

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int d = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            pq.add(new Pair(d, w));
        }

        while (!pq.isEmpty()) {
            int d, w;
            d = pq.peek().d;
            w = pq.peek().w;
            pq.remove();
            if (day < d) {
                solve.add(w);
                day++;
            }
            else if (day == d) {
                if (w > solve.peek()) {
                    solve.remove();
                    solve.add(w);
                }
            }
        }

        while (!solve.isEmpty()) {
            answer += solve.remove();
        }
        System.out.println(answer);
    }
    static class Pair implements Comparable<Pair> {
        int d, w;

        Pair(int d, int w) {
            this.d = d;
            this.w = w;
        }

        public int compareTo(Pair p) {
            if (this.d < p.d) {
                return -1;
            }
            else if (this.d == p.d) {
                if (this.w < p.w) {
                    return 1;
                }
            }
            return 1;
        }
    }
}