#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int findPeakElement(vector<int> &nums) {
        int n = nums.size();
        if (n <= 1) return 0;
        if (nums[0] > nums[1]) return 0;
        if (nums[n - 1] > nums[n - 2]) return n - 1;
        for (int i = 1; i < n - 1; ++i)
            if (nums[i - 1] < nums[i] and nums[i] > nums[i + 1])
                return i;
        return 0;
    }
};

int main() {
    Solution solution = Solution();

    vector<int> nums;
    int answer;

    nums = {1, 2, 3, 1};
    answer = solution.findPeakElement(nums);
    cout << answer << " " << 2 << endl;

    nums = {1, 2, 1, 3, 5, 6, 4};
    answer = solution.findPeakElement(nums);
    cout << answer << " " << "[1,5]" << endl;

    nums = {};
    answer = solution.findPeakElement(nums);
    cout << answer << " " << 0 << endl;

    nums = {1};
    answer = solution.findPeakElement(nums);
    cout << answer << " " << 0 << endl;

    nums = {2, 1};
    answer = solution.findPeakElement(nums);
    cout << answer << " " << 0 << endl;

    nums = {1, 2};
    answer = solution.findPeakElement(nums);
    cout << answer << " " << 1 << endl;

    nums = {2, 1, 2};
    answer = solution.findPeakElement(nums);
    cout << answer << " " << 0 << endl;

    nums = {1, 2, 1};
    answer = solution.findPeakElement(nums);
    cout << answer << " " << 1 << endl;

    nums = {1, 2, 3};
    answer = solution.findPeakElement(nums);
    cout << answer << " " << 2 << endl;

    return 0;
}