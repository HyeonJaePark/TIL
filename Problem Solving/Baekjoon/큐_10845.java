import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;
import java.io.*;


public class 큐_10845{
    public static void main(String[] args) throws IOException {
        Queue<Integer> queue = new LinkedList<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        int a = 0;
        for(int i = 0; i < n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String input = st.nextToken();
            if(input.contains("push")){
                a = Integer.parseInt(st.nextToken());
                queue.add(a);
            }
            else if(input.contains("pop")){
                sb.append((queue.isEmpty() ? -1 : queue.poll()) + "\n");
            }
            else if(input.contains("size")){
                sb.append(queue.size() + "\n");
            }
            else if(input.contains("empty")){
                sb.append((queue.isEmpty() ? 1 : 0) + "\n");
            }
            else if(input.contains("front")){
                sb.append((queue.isEmpty() ? -1 : queue.peek()) + "\n");
            }
            else if(input.contains("back")){
                sb.append((queue.isEmpty() ? -1 : a) + "\n");
            }
        }
        System.out.println(sb);
    }
}