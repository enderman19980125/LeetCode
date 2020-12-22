#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
private:
    static bool cmp(const string &a, const string &b) {
        return a + b > b + a;
    }

public:
    string largestNumber(vector<int> &nums) {
        vector<string> ss(nums.size());
        for (int i = 0; i < ss.size(); ++i) ss[i] = to_string(nums[i]);
        sort(ss.begin(), ss.end(), Solution::cmp);
        string ans;
        for (auto &s:ss) ans.append(s);
        if (ans[0] == '0') ans = "0";
        return ans;
    }
};

int main() {
    vector<int> nums;
    Solution solution = Solution();
    string answer;

    nums = {10,
            2};
    answer = solution.largestNumber(nums);
    cout << answer << " " << "210" << endl;

    nums = {3, 30, 34, 5, 9};
    answer = solution.largestNumber(nums);
    cout << answer << " " << "9534330" << endl;

    nums = {1};
    answer = solution.largestNumber(nums);
    cout << answer << " " << "1" << endl;

    nums = {10};
    answer = solution.largestNumber(nums);
    cout << answer << " " << "10" << endl;

    nums = {0, 0};
    answer = solution.largestNumber(nums);
    cout << answer << " " << "0" << endl;

    nums = {1, 0};
    answer = solution.largestNumber(nums);
    cout << answer << " " << "10" << endl;

    return 0;
}