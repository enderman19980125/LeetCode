#include <iostream>

using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        if (s.empty()) return "";
        int posLeft = 0, posRight = int(s.size()) - 1;
        while (posLeft < posRight and s[posLeft] == ' ') posLeft++;
        while (posLeft < posRight and s[posRight] == ' ') posRight--;
        if (posLeft == posRight and s[posLeft] == ' ') return "";

        string ans;
        while (posLeft <= posRight) {
            int i = posRight;
            while (posLeft <= i - 1 and s[i - 1] != ' ') i--;
            if (not ans.empty()) ans.append(" ");
            ans.append(s.substr(i, posRight - i + 1));
            posRight = i - 2;
            while (posLeft <= posRight and s[posRight] == ' ') posRight--;
        }

        return ans;
    }
};

int main() {
    Solution solution = Solution();

    string answer;

    answer = solution.reverseWords("the sky is blue");
    cout << "[" << answer << "] [" << "blue is sky the" << "]" << endl;

    answer = solution.reverseWords("  hello world!  ");
    cout << "[" << answer << "] [" << "world! hello" << "]" << endl;

    answer = solution.reverseWords("a good   example");
    cout << "[" << answer << "] [" << "example good a" << "]" << endl;

    answer = solution.reverseWords("");
    cout << "[" << answer << "] [" << "" << "]" << endl;

    answer = solution.reverseWords(" ");
    cout << "[" << answer << "] [" << "" << "]" << endl;

    answer = solution.reverseWords("   ");
    cout << "[" << answer << "] [" << "" << "]" << endl;

    answer = solution.reverseWords("  a  ");
    cout << "[" << answer << "] [" << "a" << "]" << endl;

    answer = solution.reverseWords("  a-  b-  ");
    cout << "[" << answer << "] [" << "b- a-" << "]" << endl;

    answer = solution.reverseWords("  a  b  c  ");
    cout << "[" << answer << "] [" << "c b a" << "]" << endl;

    return 0;
}