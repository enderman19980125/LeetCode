#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int majorityElement(vector<int> &nums) {
        int n = nums.size();
        unordered_map<int, int> m;
        for (int &num:nums)
            if (m.find(num) == m.end()) m[num] = 1; else m[num]++;
        for (auto &it:m) if (it.second > n / 2) return it.first;
        return 0;
    }
};

int main() {
    Solution solution = Solution();

    vector<int> nums;
    int answer;

    nums = {3, 2, 3};
    answer = solution.majorityElement(nums);
    cout << answer << " " << 3 << endl;

    nums = {2, 2, 1, 1, 1, 2, 2};
    answer = solution.majorityElement(nums);
    cout << answer << " " << 2 << endl;

    nums = {1};
    answer = solution.majorityElement(nums);
    cout << answer << " " << 1 << endl;

    nums = {1, 1};
    answer = solution.majorityElement(nums);
    cout << answer << " " << 1 << endl;

    nums = {1, 1, 1};
    answer = solution.majorityElement(nums);
    cout << answer << " " << 1 << endl;

    return 0;
}