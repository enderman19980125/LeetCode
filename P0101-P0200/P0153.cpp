#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int findMin(vector<int> &nums) {
        if (nums.empty()) return 0;
        if (nums.size() == 1) return nums[0];
        int n = nums.size(), i = 1, j = n - 1, minValue = nums[0];
        while (i < j) {
            int mid = (i + j) / 2;
            if (nums[mid] > nums[0]) i = mid + 1; else j = mid;
        }
        minValue = min(minValue, nums[i]);
        return minValue;
    }
};

int main() {
    Solution solution = Solution();

    vector<int> nums;
    int answer;

    nums = {3, 4, 5, 1, 2};
    answer = solution.findMin(nums);
    cout << answer << " " << 1 << endl;

    nums = {4, 5, 6, 7, 0, 1, 2};
    answer = solution.findMin(nums);
    cout << answer << " " << 0 << endl;

    nums = {};
    answer = solution.findMin(nums);
    cout << answer << " " << 0 << endl;

    nums = {1};
    answer = solution.findMin(nums);
    cout << answer << " " << 1 << endl;

    nums = {1, 2};
    answer = solution.findMin(nums);
    cout << answer << " " << 1 << endl;

    nums = {2, 1};
    answer = solution.findMin(nums);
    cout << answer << " " << 1 << endl;

    nums = {1, 2, 3};
    answer = solution.findMin(nums);
    cout << answer << " " << 1 << endl;

    nums = {2, 3, 1};
    answer = solution.findMin(nums);
    cout << answer << " " << 1 << endl;

    nums = {3, 1, 2};
    answer = solution.findMin(nums);
    cout << answer << " " << 1 << endl;

    nums = {1, 2, 3, 4, 5};
    answer = solution.findMin(nums);
    cout << answer << " " << 1 << endl;

    nums = {3, 4, 5, 1, 2};
    answer = solution.findMin(nums);
    cout << answer << " " << 1 << endl;

    nums = {2, 3, 4, 5, 1};
    answer = solution.findMin(nums);
    cout << answer << " " << 1 << endl;

    return 0;
}