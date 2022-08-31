import java.util.*;

public class 같은_숫자는_싫어 {
    // answer
    public class Solution {
        public int[] solution(int []arr) {
            ArrayList<Integer> list = new ArrayList<Integer>();
            list.add(arr[0]);
            
            for (int i = 1; i < arr.length; i++)
                if (arr[i] != arr[i-1])
                    list.add(arr[i]);
            
            int[] answer = Arrays.stream(list.toArray(new Integer[0])).mapToInt(Integer::intValue).toArray();
            
            return answer;
        }
    }
    // answer
}
