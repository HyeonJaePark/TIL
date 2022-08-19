import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class 스택_10828 {
    public static void main(String[] args) throws IOException {
        Stack<Integer> stack = new Stack<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        for(int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String input = st.nextToken();
            if(input.contains("push")) {
                int a = Integer.parseInt(st.nextToken());
                stack.add(a);
            }
            else if(input.contains("pop")) {
                sb.append((stack.isEmpty() ? -1 : stack.pop()) + "\n");
            }
            else if(input.contains("size")) {
                sb.append(stack.size() + "\n");
            }
            else if(input.contains("empty")) {
                sb.append((stack.isEmpty() ? 1 : 0) + "\n");
            }
            else if(input.contains("top")) {
                sb.append((stack.isEmpty() ? -1 : stack.peek()) + "\n");
            }
        }
        System.out.println(sb);
    }
}
