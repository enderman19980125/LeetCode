#include <iostream>

using namespace std;

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ans = 0;
        for (int i = 0; i < 32; ++i) {
            if ((n & 1) == 1) ans++;
            n >>= 1;
        }
        return ans;
    }
};

int main() {
    uint32_t n, answer;
    Solution solution = Solution();

    n = 11;
    answer = solution.hammingWeight(n);
    cout << answer << " " << 3 << endl;

    n = 128;
    answer = solution.hammingWeight(n);
    cout << answer << " " << 1 << endl;

    n = 4294967293;
    answer = solution.hammingWeight(n);
    cout << answer << " " << 31 << endl;

    n = 0;
    answer = solution.hammingWeight(n);
    cout << answer << " " << 0 << endl;

    n = 4294967295;
    answer = solution.hammingWeight(n);
    cout << answer << " " << 32 << endl;

    return 0;
}