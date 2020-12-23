#include <iostream>
#include <vector>

using namespace std;

class Solution {
private:
    void swap(vector<int> &nums, int s1, int t1, int s2, int t2) {
        for (int i = s1, j = s2; i <= t1 and j <= t2; ++i, ++j) std::swap(nums[i], nums[j]);
        int l1 = t1 - s1 + 1, l2 = t2 - s2 + 1;
        if (l1 == l2) return;
        if (l1 > l2)
            swap(nums, s1 + l2, t1, s2, t2);
        else
            swap(nums, s2, s2 + l1 - 1, s2 + l1, t2);
    }

public:
    void rotate(vector<int> &nums, int k) {
        int n = nums.size();
        k %= n;
        if (k == 0) return;
        swap(nums, 0, n - k - 1, n - k, n - 1);
    }
};

string to_string(vector<int> &s) {
    string ans = "[";
    for (auto &i:s) ans.append(to_string(i) + ",");
    if (not s.empty()) ans = ans.substr(0, ans.size() - 1);
    ans.append("]");
    return ans;
}

int main() {
    int k;
    vector<int> nums;
    Solution solution = Solution();

    k = 3;
    nums = {1, 2, 3, 4, 5, 6, 7};
    solution.rotate(nums, k);
    cout << to_string(nums) << " " << "[5,6,7,1,2,3,4]" << endl;

    k = 2;
    nums = {-1, -100, 3, 99};
    solution.rotate(nums, k);
    cout << to_string(nums) << " " << "[3,99,-1,-100]" << endl;

    k = 0;
    nums = {1, 2, 3, 4, 5, 6, 7};
    solution.rotate(nums, k);
    cout << to_string(nums) << " " << "[1,2,3,4,5,6,7]" << endl;

    k = 1;
    nums = {1, 2, 3, 4, 5, 6, 7};
    solution.rotate(nums, k);
    cout << to_string(nums) << " " << "[7,1,2,3,4,5,6]" << endl;

    k = 6;
    nums = {1, 2, 3, 4, 5, 6, 7};
    solution.rotate(nums, k);
    cout << to_string(nums) << " " << "[2,3,4,5,6,7,1]" << endl;

    k = 7;
    nums = {1, 2, 3, 4, 5, 6, 7};
    solution.rotate(nums, k);
    cout << to_string(nums) << " " << "[1,2,3,4,5,6,7]" << endl;

    k = 8;
    nums = {1, 2, 3, 4, 5, 6, 7};
    solution.rotate(nums, k);
    cout << to_string(nums) << " " << "[7,1,2,3,4,5,6]" << endl;

    k = 0;
    nums = {1};
    solution.rotate(nums, k);
    cout << to_string(nums) << " " << "[1]" << endl;

    k = 1;
    nums = {1};
    solution.rotate(nums, k);
    cout << to_string(nums) << " " << "[1]" << endl;

    k = 2;
    nums = {1};
    solution.rotate(nums, k);
    cout << to_string(nums) << " " << "[1]" << endl;

    k = 3;
    nums = {1};
    solution.rotate(nums, k);
    cout << to_string(nums) << " " << "[1]" << endl;

    k = 0;
    nums = {1, 2};
    solution.rotate(nums, k);
    cout << to_string(nums) << " " << "[1,2]" << endl;

    k = 1;
    nums = {1, 2};
    solution.rotate(nums, k);
    cout << to_string(nums) << " " << "[2,1]" << endl;

    k = 2;
    nums = {1, 2};
    solution.rotate(nums, k);
    cout << to_string(nums) << " " << "[1,2]" << endl;

    k = 3;
    nums = {1, 2};
    solution.rotate(nums, k);
    cout << to_string(nums) << " " << "[2,1]" << endl;

    return 0;
}