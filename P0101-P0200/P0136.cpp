#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int> &nums) {
        int m = 0;
        for (int &num:nums) m ^= num;
        return m;
    }
};

int main() {
    Solution solution = Solution();

    vector<int> nums;
    int answer;

    nums = {2, 2, 1};
    answer = solution.singleNumber(nums);
    cout << answer << " " << 1 << endl;

    nums = {4, 1, 2, 1, 2};
    answer = solution.singleNumber(nums);
    cout << answer << " " << 4 << endl;

    nums = {1};
    answer = solution.singleNumber(nums);
    cout << answer << " " << 1 << endl;

    nums = {-1};
    answer = solution.singleNumber(nums);
    cout << answer << " " << -1 << endl;

    nums = {-4, 1, 2, 1, 2};
    answer = solution.singleNumber(nums);
    cout << answer << " " << -4 << endl;

    nums = {-4, -1, 2, -1, 2};
    answer = solution.singleNumber(nums);
    cout << answer << " " << -4 << endl;

    return 0;
}