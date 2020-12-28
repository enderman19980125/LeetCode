#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int rob(vector<int> &nums) {
        int n = nums.size();
        if (n == 0) return 0;
        if (n == 1) return nums[0];

        int dp[n][2];
        dp[0][0] = 0, dp[0][1] = nums[0];
        dp[1][0] = nums[0], dp[1][1] = nums[1];
        for (int i = 2; i < n; ++i) {
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]);
            dp[i][1] = max(dp[i - 2][1], dp[i - 1][0]) + nums[i];
        }

        return max(dp[n - 1][0], dp[n - 1][1]);
    }
};

int main() {
    vector<int> nums;
    int answer;
    Solution solution = Solution();

    nums = {1, 2, 3, 1};
    answer = solution.rob(nums);
    cout << answer << " " << 4 << endl;

    nums = {2, 7, 9, 3, 1};
    answer = solution.rob(nums);
    cout << answer << " " << 12 << endl;

    nums = {};
    answer = solution.rob(nums);
    cout << answer << " " << 0 << endl;

    nums = {1};
    answer = solution.rob(nums);
    cout << answer << " " << 1 << endl;

    nums = {1, 2};
    answer = solution.rob(nums);
    cout << answer << " " << 2 << endl;

    nums = {2, 1};
    answer = solution.rob(nums);
    cout << answer << " " << 2 << endl;

    nums = {1, 2, 3};
    answer = solution.rob(nums);
    cout << answer << " " << 4 << endl;

    nums = {1, 5, 3};
    answer = solution.rob(nums);
    cout << answer << " " << 5 << endl;

    nums = {1, 1, 10, 1, 1, 10, 1, 1};
    answer = solution.rob(nums);
    cout << answer << " " << 22 << endl;

    return 0;
}