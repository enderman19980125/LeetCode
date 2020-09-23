#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

class SolutionSort {
public:
    int longestConsecutive(vector<int> &nums) {
        if (nums.empty()) return 0;
        sort(nums.begin(), nums.end());
        int maxConsecutive = 1, consecutive = 1;
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i - 1] != nums[i]) {
                if (nums[i - 1] + 1 == nums[i]) consecutive++; else consecutive = 1;
            }
            maxConsecutive = max(maxConsecutive, consecutive);
        }
        return maxConsecutive;
    }
};

class Solution {
public:
    int longestConsecutive(vector<int> &nums) {
        if (nums.empty()) return 0;
        unordered_set<int> s;
        int maxConsecutive = 1;
        for (int &num:nums) s.insert(num);
        for (int &num:nums) {
            int cntNum = num, consecutive = 1;
            if (s.find(cntNum + 1) == s.end()) {
                while (s.count(cntNum - 1) > 0) cntNum--, consecutive++;
                maxConsecutive = max(maxConsecutive, consecutive);
            }
        }
        return maxConsecutive;
    }
};

int main() {
    Solution solution = Solution();

    vector<int> nums;
    int answer;

    nums = {100, 4, 200, 1, 3, 2};
    answer = solution.longestConsecutive(nums);
    cout << answer << " " << 4 << endl;

    nums = {1, 2, 0, 1};
    answer = solution.longestConsecutive(nums);
    cout << answer << " " << 3 << endl;

    nums = {};
    answer = solution.longestConsecutive(nums);
    cout << answer << " " << 0 << endl;

    nums = {1};
    answer = solution.longestConsecutive(nums);
    cout << answer << " " << 1 << endl;

    nums = {10, 9, 1};
    answer = solution.longestConsecutive(nums);
    cout << answer << " " << 2 << endl;

    return 0;
}