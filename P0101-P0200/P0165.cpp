#include <iostream>
#include <vector>

using namespace std;

class Solution {
private:
    static void split(const string &s, vector<int> &v) {
        int p = 0;
        for (int i = 0; i < s.size(); ++i)
            if (s[i] == '.') {
                v.emplace_back(stoi(s.substr(p, i - p)));
                p = i + 1;
            }
        v.emplace_back(stoi(s.substr(p, s.size() - p)));
    }

public:
    int compareVersion(const string &version1, const string &version2) {
        vector<int> v1, v2;
        Solution::split(version1, v1);
        Solution::split(version2, v2);
        if (v1.empty()) return 2;
        while (not v1.empty() and *v1.rbegin() == 0) v1.pop_back();
        while (not v2.empty() and *v2.rbegin() == 0) v2.pop_back();
        int n = min(v1.size(), v2.size());
        for (int i = 0; i < n; ++i) {
            if (v1[i] < v2[i]) return -1;
            if (v1[i] > v2[i]) return 1;
        }
        if (v1.size() > n) return 1;
        if (v2.size() > n) return -1;
        return 0;
    }
};

int main() {
    Solution solution = Solution();

    int answer;

    answer = solution.compareVersion("1.01", "1.001");
    cout << answer << " " << 0 << endl;

    answer = solution.compareVersion("1.0", "1.0.0");
    cout << answer << " " << 0 << endl;

    answer = solution.compareVersion("0.1", "1.1");
    cout << answer << " " << -1 << endl;

    answer = solution.compareVersion("1.0.1", "1");
    cout << answer << " " << 1 << endl;

    answer = solution.compareVersion("7.5.2.4", "7.5.3");
    cout << answer << " " << -1 << endl;

    answer = solution.compareVersion("1", "0");
    cout << answer << " " << 1 << endl;

    answer = solution.compareVersion("1.2.3", "1.2.3.4");
    cout << answer << " " << -1 << endl;

    answer = solution.compareVersion("1.2.3", "1.2.3.0");
    cout << answer << " " << 0 << endl;

    return 0;
}