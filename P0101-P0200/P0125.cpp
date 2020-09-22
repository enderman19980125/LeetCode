#include <iostream>

using namespace std;

class Solution {
private:
    static bool isAlphaNumeric(char &c) {
        if ('a' <= c and c <= 'z') return true;
        if ('A' <= c and c <= 'Z') return true;
        if ('0' <= c and c <= '9') return true;
        return false;
    }

    static bool isSameAlpha(char &c1, char &c2) {
        if ('a' <= c1 and c1 <= 'z' and 'a' <= c2 and c2 <= 'z') return c1 == c2;
        if ('a' <= c1 and c1 <= 'z' and 'A' <= c2 and c2 <= 'Z') return c2 - c1 == 'A' - 'a';
        if ('A' <= c1 and c1 <= 'Z' and 'a' <= c2 and c2 <= 'z') return c1 - c2 == 'A' - 'a';
        if ('A' <= c1 and c1 <= 'Z' and 'A' <= c2 and c2 <= 'Z') return c1 == c2;
        if ('0' <= c1 and c1 <= '9' and '0' <= c2 and c2 <= '9') return c1 == c2;
        return false;
    }

public:
    bool isPalindrome(string s) {
        if (s.empty()) return true;
        int i = 0, j = s.size();
        while (i <= j) {
            while (i < s.size() and not Solution::isAlphaNumeric(s[i])) ++i;
            while (j >= 0 and not Solution::isAlphaNumeric(s[j])) --j;
            if (i == s.size() or j == -1) return true;
            if (not Solution::isSameAlpha(s[i], s[j])) return false;
            ++i, --j;
        }
        return true;
    }
};

int main() {
    Solution solution = Solution();

    bool answer;

    answer = solution.isPalindrome("A man, a plan, a canal: Panama");
    cout << answer << " " << true << endl;

    answer = solution.isPalindrome("race a car");
    cout << answer << " " << false << endl;

    answer = solution.isPalindrome("");
    cout << answer << " " << true << endl;

    answer = solution.isPalindrome(" ");
    cout << answer << " " << true << endl;

    answer = solution.isPalindrome("0P");
    cout << answer << " " << false << endl;

    answer = solution.isPalindrome("1b1");
    cout << answer << " " << true << endl;

    answer = solution.isPalindrome("a");
    cout << answer << " " << true << endl;

    answer = solution.isPalindrome(" a A ");
    cout << answer << " " << true << endl;

    answer = solution.isPalindrome(" B*&a A b@!#");
    cout << answer << " " << true << endl;

    return 0;
}