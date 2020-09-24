#include <iostream>

using namespace std;

class Solution {
public:
    int minCut(string s) {
        int n = s.size();
        if (n <= 1) return 0;

        bool isPalindrome[n][n];
        for (int j = 0; j < n; ++j)
            for (int i = 0; i <= j; ++i) {
                if (i == j) {
                    isPalindrome[i][j] = true;
                    continue;
                }
                if (i + 1 == j) {
                    isPalindrome[i][j] = s[i] == s[j];
                    continue;
                }
                isPalindrome[i][j] = isPalindrome[i + 1][j - 1] & (s[i] == s[j]);
            }

        int dp[n];
        for (int i = 0; i < n; ++i) {
            dp[i] = isPalindrome[0][i] ? 1 : n;
            for (int j = 0; j < i; ++j) if (isPalindrome[j + 1][i]) dp[i] = min(dp[i], dp[j] + 1);
        }
        return dp[n - 1] - 1;
    }
};

int main() {
    Solution solution = Solution();

    int answer;

    answer = solution.minCut("aab");
    cout << answer << " " << 1 << endl;

    answer = solution.minCut("a");
    cout << answer << " " << 0 << endl;

    answer = solution.minCut("ab");
    cout << answer << " " << 1 << endl;

    answer = solution.minCut("");
    cout << answer << " " << 0 << endl;

    answer = solution.minCut("ababc");
    cout << answer << " " << 2 << endl;

    return 0;
}