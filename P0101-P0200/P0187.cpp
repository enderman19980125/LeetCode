#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<string> findRepeatedDnaSequences(string &s) {
        if (s.size() <= 10) return vector<string>{};

        unordered_map<string, int> mp;
        for (int k = 0; k <= s.size() - 10; ++k) {
            string pattern = s.substr(k, 10);
            if (mp.find(pattern) == mp.end())
                mp[pattern] = 1;
            else
                mp[pattern]++;
        }

        vector<string> ans;
        for (auto &it:mp) if (it.second >= 2) ans.emplace_back(it.first);
        return ans;
    }
};

string to_string(vector<string> &s) {
    string ans = "[";
    for (auto &i:s) ans.append(i + ",");
    if (not s.empty()) ans = ans.substr(0, ans.size() - 1);
    ans.append("]");
    return ans;
}

int main() {
    string s;
    Solution solution = Solution();
    vector<string> answer;

    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT";
    answer = solution.findRepeatedDnaSequences(s);
    cout << to_string(answer) << " " << "[AAAAACCCCC,CCCCCAAAAA]" << endl;

    s = "AAAAAAAAAAAAA";
    answer = solution.findRepeatedDnaSequences(s);
    cout << to_string(answer) << " " << "[AAAAAAAAAA]" << endl;

    s = "AAAAAAAAAA";
    answer = solution.findRepeatedDnaSequences(s);
    cout << to_string(answer) << " " << "[]" << endl;

    s = "AAAAAAAAAAA";
    answer = solution.findRepeatedDnaSequences(s);
    cout << to_string(answer) << " " << "[AAAAAAAAAA]" << endl;

    return 0;
}