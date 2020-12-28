class Solution {
    public int countPrimes(int n) {
        int ans = 0;
        int[] a = new int[n];

        for (int i = 2; i < n; ++i)
            if (a[i] == 0) {
                ans++;
                for (int j = 2 * i; j < n; j += i) a[j] = 1;
            }

        return ans;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int answer;

        answer = solution.countPrimes(10);
        System.out.printf("%d %d\n", answer, 4);

        answer = solution.countPrimes(0);
        System.out.printf("%d %d\n", answer, 0);

        answer = solution.countPrimes(1);
        System.out.printf("%d %d\n", answer, 0);

        answer = solution.countPrimes(2);
        System.out.printf("%d %d\n", answer, 0);

        answer = solution.countPrimes(20);
        System.out.printf("%d %d\n", answer, 8);

        answer = solution.countPrimes(100);
        System.out.printf("%d %d\n", answer, 25);

        answer = solution.countPrimes(1000);
        System.out.printf("%d %d\n", answer, 168);

        answer = solution.countPrimes(5000000);
        System.out.printf("%d %d\n", answer, 348513);
    }
}