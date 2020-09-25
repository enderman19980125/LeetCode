#include <iostream>
#include <vector>

using namespace std;

class Solution {
private:
    static bool isSameWord(string &str, string &word, int s) {
        if (s < 0) return false;
        for (int k = 0; k < word.size(); ++k) if (str[s + k] != word[k]) return false;
        return true;
    }

public:
    bool wordBreak(string s, vector<string> &wordDict) {
        int n = s.size();
        bool dp[n];

        for (int i = 0; i < n; ++i) {
            dp[i] = false;
            for (string &word:wordDict) {
                int p = i - int(word.size()) + 1;
                if (Solution::isSameWord(s, word, p) and (p == 0 or dp[p - 1])) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n - 1];
    }
};

int main() {
    Solution solution = Solution();

    string s;
    vector<string> wordDict;
    bool answer;

    s = "leetcode";
    wordDict = {"leet", "code"};
    answer = solution.wordBreak(s, wordDict);
    cout << answer << " " << true << endl;

    s = "applepenapple";
    wordDict = {"apple", "pen"};
    answer = solution.wordBreak(s, wordDict);
    cout << answer << " " << true << endl;

    s = "catsandog";
    wordDict = {"cats", "dog", "sand", "and", "cat"};
    answer = solution.wordBreak(s, wordDict);
    cout << answer << " " << false << endl;

    s = "c";
    wordDict = {"a", "b"};
    answer = solution.wordBreak(s, wordDict);
    cout << answer << " " << false << endl;

    s = "c";
    wordDict = {"a", "b", "c"};
    answer = solution.wordBreak(s, wordDict);
    cout << answer << " " << true << endl;

    return 0;
}