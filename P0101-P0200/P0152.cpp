#include <iostream>
#include <vector>

using namespace std;

class Solution {
private:
    int maxProductFromTo(vector<int> &nums, int left, int right) {
        if (left == right) return nums[left];

        int allValue = 1;
        for (int i = left; i <= right; ++i) allValue *= nums[i];
        if (allValue > 0) return allValue;

        int i = left, leftValue = 1, j = right, rightValue = 1;
        while (i < right and nums[i] > 0) leftValue *= nums[i++];
        while (left < j and nums[j] > 0) rightValue *= nums[j--];
        int maxValue = max(leftValue, rightValue);

        leftValue *= nums[i];
        rightValue *= nums[j];
        maxValue = max(maxValue, allValue / leftValue);
        maxValue = max(maxValue, allValue / rightValue);

        return maxValue;
    }

public:
    int maxProduct(vector<int> &nums) {
        if (nums.empty()) return 0;
        int maxValue = nums[0], left = 0, n = nums.size();
        for (int right = 0; right < n; ++right) {
            if (nums[right] == 0 and left < right) {
                maxValue = max(maxValue, 0);
                maxValue = max(maxValue, this->maxProductFromTo(nums, left, right - 1));
            }
            if (nums[right] == 0) left = right + 1;
        }
        if (left <= n - 1) maxValue = max(maxValue, this->maxProductFromTo(nums, left, n - 1));
        return maxValue;
    }
};

int main() {
    Solution solution = Solution();

    vector<int> nums;
    int answer;

    nums = {2, 3, -2, 4};
    answer = solution.maxProduct(nums);
    cout << answer << " " << 6 << endl;

    nums = {-2, 0, -1};
    answer = solution.maxProduct(nums);
    cout << answer << " " << 0 << endl;

    nums = {};
    answer = solution.maxProduct(nums);
    cout << answer << " " << 0 << endl;

    nums = {1};
    answer = solution.maxProduct(nums);
    cout << answer << " " << 1 << endl;

    nums = {-1};
    answer = solution.maxProduct(nums);
    cout << answer << " " << -1 << endl;

    nums = {0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0};
    answer = solution.maxProduct(nums);
    cout << answer << " " << 1 << endl;

    nums = {0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0};
    answer = solution.maxProduct(nums);
    cout << answer << " " << 0 << endl;

    nums = {2, -1, 3, -1, 3, -1, 4};
    answer = solution.maxProduct(nums);
    cout << answer << " " << 36 << endl;

    nums = {2, -1, 3, 0, 2, -1, 4};
    answer = solution.maxProduct(nums);
    cout << answer << " " << 4 << endl;

    return 0;
}