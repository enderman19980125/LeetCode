#include <iostream>
#include <memory.h>

using namespace std;

class Solution {
public:
    int numDistinct(string s, string t) {
        int size_s = s.size(), size_t = t.size();
        unsigned int dp[size_s + 1][size_t + 1];
        memset(dp, 0, sizeof(dp));
        for (int i = 0; i <= size_s; i++) dp[i][0] = 1;
        for (int i = 1; i <= size_s; i++)
            for (int j = 1; j <= min(i, size_t); j++) {
                if (s[i - 1] == t[j - 1])
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                else
                    dp[i][j] = dp[i - 1][j];
            }
        return int(dp[size_s][size_t]);
    }
};

int main() {
    Solution solution = Solution();

    int answer;

    answer = solution.numDistinct("rabbbit", "rabbit");
    cout << answer << " " << 3 << endl;

    answer = solution.numDistinct("babgbag", "bag");
    cout << answer << " " << 5 << endl;

    answer = solution.numDistinct(
            "xslledayhxhadmctrliaxqpokyezcfhzaskeykchkmhpyjipxtsuljkwkovmvelvwxzwieeuqnjozrfwmzsylcwvsthnxujvrkszqwtglewkycikdaiocglwzukwovsghkhyidevhbgffoqkpabthmqihcfxxzdejletqjoxmwftlxfcxgxgvpperwbqvhxgsbbkmphyomtbjzdjhcrcsggleiczpbfjcgtpycpmrjnckslrwduqlccqmgrdhxolfjafmsrfdghnatexyanldrdpxvvgujsztuffoymrfteholgonuaqndinadtumnuhkboyzaqguwqijwxxszngextfcozpetyownmyneehdwqmtpjloztswmzzdzqhuoxrblppqvyvsqhnhryvqsqogpnlqfulurexdtovqpqkfxxnqykgscxaskmksivoazlducanrqxynxlgvwonalpsyddqmaemcrrwvrjmjjnygyebwtqxehrclwsxzylbqexnxjcgspeynlbmetlkacnnbhmaizbadynajpibepbuacggxrqavfnwpcwxbzxfymhjcslghmajrirqzjqxpgtgisfjreqrqabssobbadmtmdknmakdigjqyqcruujlwmfoagrckdwyiglviyyrekjealvvigiesnvuumxgsveadrxlpwetioxibtdjblowblqvzpbrmhupyrdophjxvhgzclidzybajuxllacyhyphssvhcffxonysahvzhzbttyeeyiefhunbokiqrpqfcoxdxvefugapeevdoakxwzykmhbdytjbhigffkmbqmqxsoaiomgmmgwapzdosorcxxhejvgajyzdmzlcntqbapbpofdjtulstuzdrffafedufqwsknumcxbschdybosxkrabyfdejgyozwillcxpcaiehlelczioskqtptzaczobvyojdlyflilvwqgyrqmjaeepydrcchfyftjighntqzoo",
            "rwmimatmhydhbujebqehjprrwfkoebcxxqfktayaaeheys"
    );
    cout << answer << " " << 543744000 << endl;

    answer = solution.numDistinct("", "");
    cout << answer << " " << 1 << endl;

    answer = solution.numDistinct("", "a");
    cout << answer << " " << 0 << endl;

    answer = solution.numDistinct("a", "");
    cout << answer << " " << 1 << endl;

    answer = solution.numDistinct("aaa", "");
    cout << answer << " " << 1 << endl;

    answer = solution.numDistinct("aaa", "a");
    cout << answer << " " << 3 << endl;

    answer = solution.numDistinct("aaabb", "ab");
    cout << answer << " " << 6 << endl;

    return 0;
}