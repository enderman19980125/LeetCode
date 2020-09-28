#include <iostream>

using namespace std;

class Solution {
public:
    int titleToNumber(const string &s) {
        int n = s.size(), k = 0, sumK = 1, ans = 0;
        while (k < n - 1) {
            k++;
            sumK *= 26;
            ans += sumK;
        }
        for (int i = 0; i < n; ++i) {
            ans += (s[i] - 'A') * sumK;
            k--;
            sumK /= 26;
        }
        ans++;
        return ans;
    }
};

int main() {
    Solution solution = Solution();

    int answer;

    answer = solution.titleToNumber("A");
    cout << answer << " " << 1 << endl;

    answer = solution.titleToNumber("AB");
    cout << answer << " " << 28 << endl;

    answer = solution.titleToNumber("ZY");
    cout << answer << " " << 701 << endl;

    answer = solution.titleToNumber("CFDGSXM");
    cout << answer << " " << 1000000001 << endl;

    answer = solution.titleToNumber("Z");
    cout << answer << " " << 26 << endl;

    answer = solution.titleToNumber("AA");
    cout << answer << " " << 27 << endl;

    answer = solution.titleToNumber("ZZ");
    cout << answer << " " << 702 << endl;

    answer = solution.titleToNumber("AAA");
    cout << answer << " " << 703 << endl;

    answer = solution.titleToNumber("B");
    cout << answer << " " << 2 << endl;

    answer = solution.titleToNumber("C");
    cout << answer << " " << 3 << endl;

    answer = solution.titleToNumber("X");
    cout << answer << " " << 24 << endl;

    answer = solution.titleToNumber("Y");
    cout << answer << " " << 25 << endl;

    answer = solution.titleToNumber("SZ");
    cout << answer << " " << 520 << endl;

    answer = solution.titleToNumber("GIS");
    cout << answer << " " << 4985 << endl;

    return 0;
}