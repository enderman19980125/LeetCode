#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    string fractionToDecimal(long long numerator, long long denominator) {
        string ans;
        if (numerator * denominator < 0) ans.append("-");
        numerator = abs(numerator), denominator = abs(denominator);
        ans.append(to_string(numerator / denominator));
        if (numerator % denominator == 0) return ans;
        numerator %= denominator;
        ans.append(".");

        unordered_map<long long, long long> m;
        while (true) {
            numerator *= 10;
            if (numerator == 0) break;
            if (m.find(numerator) != m.end()) {
                int pos = m[numerator], n = ans.size();
                ans = ans.substr(0, pos) + "(" + ans.substr(pos, n - pos) + ")";
                break;
            }
            m[numerator] = ans.size();
            long long p = numerator / denominator;
            long long r = numerator % denominator;
            numerator = r;
            ans.append(to_string(p));
        }
        return ans;
    }
};

int main() {
    Solution solution = Solution();

    string answer;

    answer = solution.fractionToDecimal(1, 2);
    cout << answer << " " << "0.5" << endl;

    answer = solution.fractionToDecimal(2, 1);
    cout << answer << " " << "2" << endl;

    answer = solution.fractionToDecimal(2, 3);
    cout << answer << " " << "0.(6)" << endl;

    answer = solution.fractionToDecimal(4, 333);
    cout << answer << " " << "0.(012)" << endl;

    answer = solution.fractionToDecimal(1, 5);
    cout << answer << " " << "0.2" << endl;

    answer = solution.fractionToDecimal(0, 5);
    cout << answer << " " << "0" << endl;

    answer = solution.fractionToDecimal(10, 2);
    cout << answer << " " << "5" << endl;

    answer = solution.fractionToDecimal(100, 7);
    cout << answer << " " << "14.(285714)" << endl;

    answer = solution.fractionToDecimal(10000, 111);
    cout << answer << " " << "90.(090)" << endl;

    answer = solution.fractionToDecimal(-10, 3);
    cout << answer << " " << "-3.(3)" << endl;

    answer = solution.fractionToDecimal(10, -3);
    cout << answer << " " << "-3.(3)" << endl;

    answer = solution.fractionToDecimal(-10, -3);
    cout << answer << " " << "3.(3)" << endl;

    answer = solution.fractionToDecimal(-100, 77);
    cout << answer << " " << "-1.(298701)" << endl;

    answer = solution.fractionToDecimal(INT_MAX, INT_MAX);
    cout << answer << " " << "1" << endl;

    return 0;
}