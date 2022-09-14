public class k진수에서_소수_개수_구하기 {
    public static void main(String[] args) {
        int N = 170179;
        int K = 10;

        Solution s = new Solution();
        System.out.println(s.solution(N, K));
    }
    static class Solution {
        public int solution(int n, int k) {
            int answer = 0;
            String convertedN = Integer.toString(n, k);
            System.out.println(convertedN);
            String[] splitedN = convertedN.split("0");
            for (String s : splitedN) {
                if (s.length() > 0) {
                    System.out.println(s);
                    if (isPrime(s)) answer++;
                }
            }
            return answer;
        }

        static boolean isPrime(String n) {
            long convertedToInt = Long.parseLong(n);

            if (convertedToInt == 1) return false;

            for (long i = 2; i * i <= convertedToInt; i++) {
                if (convertedToInt % i == 0) return false;
            }

            return true;
        }
    }
}