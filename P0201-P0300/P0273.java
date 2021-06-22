 class Solution {
    public String numberToWords(int num) {
        if (num == 0) return "Zero";
        if (num == 1) return "One";
        if (num == 2) return "Two";
        if (num == 3) return "Three";
        if (num == 4) return "Four";
        if (num == 5) return "Five";
        if (num == 6) return "Six";
        if (num == 7) return "Seven";
        if (num == 8) return "Eight";
        if (num == 9) return "Nine";

        if (num == 10) return "Ten";
        if (num == 11) return "Eleven";
        if (num == 12) return "Twelve";
        if (num == 13) return "Thirteen";
        if (num == 14) return "Fourteen";
        if (num == 15) return "Fifteen";
        if (num == 16) return "Sixteen";
        if (num == 17) return "Seventeen";
        if (num == 18) return "Eighteen";
        if (num == 19) return "Nineteen";

        if (num == 20) return "Twenty";
        if (num == 30) return "Thirty";
        if (num == 40) return "Forty";
        if (num == 50) return "Fifty";
        if (num == 60) return "Sixty";
        if (num == 70) return "Seventy";
        if (num == 80) return "Eighty";
        if (num == 90) return "Ninety";

        if (num >= 1000000000) {
            if (num % 1000000000 == 0) return numberToWords(num / 1000000000) + " Billion";
            return numberToWords(num / 1000000000) + " Billion " + numberToWords(num % 1000000000);
        }
        if (num >= 1000000) {
            if (num % 1000000 == 0) return numberToWords(num / 1000000) + " Million";
            return numberToWords(num / 1000000) + " Million " + numberToWords(num % 1000000);
        }
        if (num >= 1000) {
            if (num % 1000 == 0) return numberToWords(num / 1000) + " Thousand";
            return numberToWords(num / 1000) + " Thousand " + numberToWords(num % 1000);
        }
        if (num >= 100) {
            if (num % 100 == 0) return numberToWords(num / 100) + " Hundred";
            return numberToWords(num / 100) + " Hundred " + numberToWords(num % 100);
        }
        return numberToWords(num / 10 * 10) + " " + numberToWords(num % 10);
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        String answer, stdAnswer;

        stdAnswer = "One Hundred Twenty Three";
        answer = solution.numberToWords(123);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        stdAnswer = "Twelve Thousand Three Hundred Forty Five";
        answer = solution.numberToWords(12345);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        stdAnswer = "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven";
        answer = solution.numberToWords(1234567);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        stdAnswer = "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One";
        answer = solution.numberToWords(1234567891);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        stdAnswer = "One Hundred";
        answer = solution.numberToWords(100);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        stdAnswer = "Two Hundred";
        answer = solution.numberToWords(200);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);
    }
}