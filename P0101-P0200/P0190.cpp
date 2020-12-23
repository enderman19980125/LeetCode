#include <iostream>

using namespace std;

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t ans = 0;
        for (int i = 0; i < 32; ++i) {
            uint32_t b = n & 1;
            ans = (ans << 1) + b;
            n >>= 1;
        }
        return ans;
    }
};

int main() {
    uint32_t n, answer;
    Solution solution = Solution();

    n = 43261596;
    answer = solution.reverseBits(n);
    cout << answer << " " << 964176192 << endl;

    n = 4294967293;
    answer = solution.reverseBits(n);
    cout << answer << " " << 3221225471 << endl;

    n = 0;
    answer = solution.reverseBits(n);
    cout << answer << " " << 0 << endl;

    n = 1;
    answer = solution.reverseBits(n);
    cout << answer << " " << 2147483648 << endl;

    n = 2147483648;
    answer = solution.reverseBits(n);
    cout << answer << " " << 1 << endl;

    return 0;
}