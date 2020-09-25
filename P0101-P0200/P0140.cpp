#include <iostream>
#include <vector>

using namespace std;

class Solution {
private:
    static bool isSameWord(string &s, string &word, int p) {
        for (int k = 0; k < word.size(); ++k) if (p + k == s.size() or s[p + k] != word[k]) return false;
        return true;
    }

    void generate(int k, const string &cntString, vector<string> &ans, int &n, vector<int> dp[],
                  vector<string> &wordDict) {
        if (k == n) {
            ans.push_back(cntString);
            return;
        }
        for (int wordIndex:dp[k]) {
            string &word = wordDict[wordIndex];
            string nextString = cntString;
            if (not nextString.empty()) nextString.append(" ");
            nextString.append(word);
            this->generate(k + int(word.size()), nextString, ans, n, dp, wordDict);
        }
    }

public:
    vector<string> wordBreak(string &s, vector<string> &wordDict) {
        int n = s.size(), maxReach = 0;
        vector<int> dp[n];
        vector<string> ans;

        for (int i = 0; i < n; ++i) {
            for (int k = 0; k < wordDict.size(); ++k)
                if (Solution::isSameWord(s, wordDict[k], i)) {
                    dp[i].emplace_back(k);
                    maxReach = max(maxReach, i + int(wordDict[k].size()) - 1);
                }
            if (maxReach < i and dp[i].empty()) return ans;
        }

        this->generate(0, "", ans, n, dp, wordDict);
        return ans;
    }
};

string to_string(vector<string> &stringVector) {
    string s = "[";
    for (string &ss:stringVector) s += ss + ", ";
    if (not stringVector.empty()) s = s.substr(0, s.size() - 2);
    s += "]";
    return s;
}

int main() {
    Solution solution = Solution();

    string s;
    vector<string> wordDict;
    vector<string> answer;

    s = "catsanddog";
    wordDict = {"cat", "cats", "and", "sand", "dog"};
    answer = solution.wordBreak(s, wordDict);
    cout << to_string(answer) << " " << "[cats and dog, cat sand dog]" << endl;

    s = "pineapplepenapple";
    wordDict = {"apple", "pen", "applepen", "pine", "pineapple"};
    answer = solution.wordBreak(s, wordDict);
    cout << to_string(answer) << " " << "[pine apple pen apple, pineapple pen apple, pine applepen apple]" << endl;

    s = "catsandog";
    wordDict = {"cats", "dog", "sand", "and", "cat"};
    answer = solution.wordBreak(s, wordDict);
    cout << to_string(answer) << " " << "[]" << endl;

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab";
    wordDict = {"a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"};
    answer = solution.wordBreak(s, wordDict);
    cout << to_string(answer) << " " << "[]" << endl;

    s = "aa";
    wordDict = {"a", "aa"};
    answer = solution.wordBreak(s, wordDict);
    cout << to_string(answer) << " " << "[a a, aa]" << endl;

    s = "a";
    wordDict = {"a"};
    answer = solution.wordBreak(s, wordDict);
    cout << to_string(answer) << " " << "[a]" << endl;

    return 0;
}