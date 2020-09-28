#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    string convertToTitle(long long n) {
        long long k = 0, sumTotal = 0, powK = 1;
        while (sumTotal + 26 * powK < n) {
            k++;
            powK *= 26;
            sumTotal += powK;
        }
        n -= sumTotal;

        vector<long long> v;
        while (k >= 0) {
            long long t = 1;
            while (t * powK < n) t++;
            t--;
            v.emplace_back(t);
            n = n - t * powK;
            k--;
            powK /= 26;
        }

        string ans;
        for (auto it:v) ans += char(it + 'A');
        return ans;
    }
};

int main() {
    Solution solution = Solution();

    string answer;

    answer = solution.convertToTitle(1);
    cout << answer << " " << "A" << endl;

    answer = solution.convertToTitle(28);
    cout << answer << " " << "AB" << endl;

    answer = solution.convertToTitle(701);
    cout << answer << " " << "ZY" << endl;

    answer = solution.convertToTitle(1000000001);
    cout << answer << " " << "CFDGSXM" << endl;

    answer = solution.convertToTitle(26);
    cout << answer << " " << "Z" << endl;

    answer = solution.convertToTitle(27);
    cout << answer << " " << "AA" << endl;

    answer = solution.convertToTitle(702);
    cout << answer << " " << "ZZ" << endl;

    answer = solution.convertToTitle(703);
    cout << answer << " " << "AAA" << endl;

    answer = solution.convertToTitle(2);
    cout << answer << " " << "B" << endl;

    answer = solution.convertToTitle(3);
    cout << answer << " " << "C" << endl;

    answer = solution.convertToTitle(24);
    cout << answer << " " << "X" << endl;

    answer = solution.convertToTitle(25);
    cout << answer << " " << "Y" << endl;

    answer = solution.convertToTitle(520);
    cout << answer << " " << "SZ" << endl;

    answer = solution.convertToTitle(4985);
    cout << answer << " " << "GIS" << endl;

    return 0;
}