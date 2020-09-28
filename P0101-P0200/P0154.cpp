#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int findMin(vector<int> &nums) {
        if (nums.empty()) return 0;
        int n = nums.size(), i = 0, j = n - 1;
        while (j > 0 and nums[j] == nums[0]) j--;
        while (i < j) {
            int mid = (i + j) / 2;
            if (nums[mid] >= nums[0]) i = mid + 1; else j = mid;
        }
        int minValue = min(nums[0], nums[i]);
        return minValue;
    }
};

int main() {
    Solution solution = Solution();

    vector<int> nums;
    int answer;

    nums = {1, 3, 5};
    answer = solution.findMin(nums);
    cout << answer << " " << 1 << endl;

    nums = {2, 2, 2, 0, 1};
    answer = solution.findMin(nums);
    cout << answer << " " << 0 << endl;

    nums = {10, 1, 10, 10, 10};
    answer = solution.findMin(nums);
    cout << answer << " " << 1 << endl;

    nums = {};
    answer = solution.findMin(nums);
    cout << answer << " " << 0 << endl;

    nums = {1};
    answer = solution.findMin(nums);
    cout << answer << " " << 1 << endl;

    nums = {1, 1};
    answer = solution.findMin(nums);
    cout << answer << " " << 1 << endl;

    nums = {1, 2};
    answer = solution.findMin(nums);
    cout << answer << " " << 1 << endl;

    nums = {2, 1};
    answer = solution.findMin(nums);
    cout << answer << " " << 1 << endl;

    nums = {1, 1, 1};
    answer = solution.findMin(nums);
    cout << answer << " " << 1 << endl;

    nums = {1, 1, 2};
    answer = solution.findMin(nums);
    cout << answer << " " << 1 << endl;

    nums = {2, 1, 1};
    answer = solution.findMin(nums);
    cout << answer << " " << 1 << endl;

    nums = {1, 2, 1};
    answer = solution.findMin(nums);
    cout << answer << " " << 1 << endl;

    nums = {1, 1, 2, 1, 1};
    answer = solution.findMin(nums);
    cout << answer << " " << 1 << endl;

    nums = {2, 1, 1, 1, 1};
    answer = solution.findMin(nums);
    cout << answer << " " << 1 << endl;

    nums = {1, 1, 1, 1, 2};
    answer = solution.findMin(nums);
    cout << answer << " " << 1 << endl;

    return 0;
}