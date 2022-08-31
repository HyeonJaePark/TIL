import java.util.*;

public class 두_큐_합_같게_만들기 {
    // answer
    class Solution {
        public int solution(int[] queue1, int[] queue2) {
            Queue<Integer> q1 = new LinkedList<>();
            Queue<Integer> q2 = new LinkedList<>();

            int answer = 0;
            long q1s = 0, q2s = 0;
            int attamp = 0;
            final int QUEUE_LENGTH = queue1.length;

            for (int i : queue1) {
                q1s += i;
                q1.add(i);
            }
            for (int i : queue2) {
                q2s += i;
                q2.add(i);
            }

            while (q1s != q2s) {
                if (attamp > QUEUE_LENGTH * 2 + 1) {
                    answer = -1;
                    break;
                }

                if (q1s > q2s) {
                    int tmp = q1.poll();
                    q1s -= tmp;
                    q2s += tmp;
                    q2.add(tmp);
                }
                else if (q1s < q2s) {
                    int tmp = q2.poll();
                    q1s += tmp;
                    q2s -= tmp;
                    q1.add(tmp);
                }
                
                attamp += 1;
                
                if (q1s == q2s) {
                    answer = attamp;
                    break;
                }
            }

            return answer;
        }
    }
    // answer
}
