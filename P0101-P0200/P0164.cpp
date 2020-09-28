#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maximumGap(vector<int> &nums) {
        int n = nums.size();
        if (n <= 1) return 0;
        sort(nums.begin(), nums.end());
        int maxGap = 0;
        for (int i = 0; i < n - 1; ++i) maxGap = max(maxGap, nums[i + 1] - nums[i]);
        return maxGap;
    }
};

int main() {
    Solution solution = Solution();

    vector<int> nums;
    int answer;

    nums = {3, 6, 9, 1};
    answer = solution.maximumGap(nums);
    cout << answer << " " << 3 << endl;

    nums = {10};
    answer = solution.maximumGap(nums);
    cout << answer << " " << 0 << endl;

    nums = {};
    answer = solution.maximumGap(nums);
    cout << answer << " " << 0 << endl;

    nums = {1, 3};
    answer = solution.maximumGap(nums);
    cout << answer << " " << 2 << endl;

    nums = {2, 8, 1, 4, 9};
    answer = solution.maximumGap(nums);
    cout << answer << " " << 4 << endl;

    return 0;
}