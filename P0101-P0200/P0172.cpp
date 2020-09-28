#include <iostream>

using namespace std;

class Solution {
public:
    int trailingZeroes(int n) {
        int c5 = 0;
        for (int i = 5; i <= n; i += 5) {
            int t = i;
            while (t % 5 == 0) t /= 5, c5++;
        }
        return c5;
    }
};

int main() {
    Solution solution = Solution();

    int answer;

    answer = solution.trailingZeroes(0);
    cout << answer << " " << 0 << endl;

    answer = solution.trailingZeroes(1);
    cout << answer << " " << 0 << endl;

    answer = solution.trailingZeroes(2);
    cout << answer << " " << 0 << endl;

    answer = solution.trailingZeroes(3);
    cout << answer << " " << 0 << endl;

    answer = solution.trailingZeroes(4);
    cout << answer << " " << 0 << endl;

    answer = solution.trailingZeroes(5);
    cout << answer << " " << 1 << endl;

    answer = solution.trailingZeroes(10);
    cout << answer << " " << 2 << endl;

    answer = solution.trailingZeroes(20);
    cout << answer << " " << 4 << endl;

    answer = solution.trailingZeroes(10000);
    cout << answer << " " << 2499 << endl;

    return 0;
}