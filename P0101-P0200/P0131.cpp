#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
private:
    static bool isPalindrome(string &s) {
        if (s.empty()) return true;
        unsigned int i = 0, j = s.size() - 1;
        while (i < j) {
            if (s[i] != s[j]) return false;
            i++, j--;
        }
        return true;
    }

    void search(int k, string &s, unordered_map<string, bool> &m, vector<string> &cnt, vector<vector<string>> &ans) {
        if (k == s.size()) {
            ans.push_back(cnt);
            return;
        }
        for (int i = k; i < s.size(); ++i) {
            string cntWord = s.substr(k, i - k + 1);
            if (m.find(cntWord) == m.end()) m[cntWord] = Solution::isPalindrome(cntWord);
            if (m[cntWord]) {
                cnt.push_back(cntWord);
                this->search(i + 1, s, m, cnt, ans);
                cnt.pop_back();
            }
        }
    }

public:
    vector<vector<string>> partition(string s) {
        unordered_map<string, bool> m;
        vector<string> cnt;
        vector<vector<string>> ans;
        if (s.empty()) return ans;
        this->search(0, s, m, cnt, ans);
        return ans;
    }
};

string to_string(vector<vector<string>> &stringVector) {
    string s = "[";
    for (auto &row:stringVector) {
        s += "[";
        for (auto &element:row) s += element + ", ";
        if (not row.empty()) s = s.substr(0, s.size() - 2);
        s += "], ";
    }
    if (not stringVector.empty()) s = s.substr(0, s.size() - 2);
    s += "]";
    return s;
}

int main() {
    Solution solution = Solution();

    vector<vector<string>> answer;

    answer = solution.partition("aab");
    cout << to_string(answer) << " " << "[[aa, b], [a, a, b]]" << endl;

    answer = solution.partition("");
    cout << to_string(answer) << " " << "[]" << endl;

    answer = solution.partition("a");
    cout << to_string(answer) << " " << "[[a]]" << endl;

    answer = solution.partition("aa");
    cout << to_string(answer) << " " << "[[a, a], [aa]]" << endl;

    answer = solution.partition("ab");
    cout << to_string(answer) << " " << "[[a, b]]" << endl;

    answer = solution.partition("ababa");
    cout << to_string(answer) << " " << "[[a, b, a, b, a], [a, b, aba], [a, bab, a], [aba, b, a], [ababa]]" << endl;

    return 0;
}