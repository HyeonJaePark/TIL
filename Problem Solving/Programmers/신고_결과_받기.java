import java.util.*;

public class 신고_결과_받기 {
    public static void main(String[] args) {
        String[] id_list = {"con", "ryan"};
        String[] report = {"ryan con", "ryan con", "ryan con", "ryan con"};
        int k = 3;
        
        int[] answer = solution(id_list, report, k);
        
        for (int i : answer) {
            System.out.print(i + " ");
        }
    }
    // answer code
    public static int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        HashMap<String, HashSet<String>> user_report_list = new HashMap<>();
        HashMap<String, Integer> answer_hashmap = new HashMap<>();

        StringTokenizer st;

        for (String id : id_list) {
            user_report_list.put(id, new HashSet<String>());
            answer_hashmap.put(id, 0);
        }

        for (String log : report) {
            st = new StringTokenizer(log);
            String reporter_user = st.nextToken();
            String reported_user = st.nextToken();
            user_report_list.get(reported_user).add(reporter_user);
        }

        for (String id : user_report_list.keySet()) {
            if (user_report_list.get(id).size() >= k) {
                for (String reporter_user : user_report_list.get(id)) {
                    answer_hashmap.put(reporter_user, answer_hashmap.get(reporter_user) + 1);
                }
            }
        }

        for (int i = 0; i < id_list.length; i++) {
            answer[i] = answer_hashmap.get(id_list[i]);
        }

        return answer;
    }
    // answer code
}