#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int> &prices) {
        if (prices.empty()) return 0;
        int n = prices.size();
        int profit = 0;
        for (int i = 1; i < n; ++i) profit += max(0, prices[i] - prices[i - 1]);
        return profit;
    }
};

int main() {
    Solution solution = Solution();

    vector<int> nums;
    int answer;

    nums = {7, 1, 5, 3, 6, 4};
    answer = solution.maxProfit(nums);
    cout << answer << " " << 7 << endl;

    nums = {1, 2, 3, 4, 5};
    answer = solution.maxProfit(nums);
    cout << answer << " " << 4 << endl;

    nums = {7, 6, 4, 3, 1};
    answer = solution.maxProfit(nums);
    cout << answer << " " << 0 << endl;

    nums = {};
    answer = solution.maxProfit(nums);
    cout << answer << " " << 0 << endl;

    nums = {1};
    answer = solution.maxProfit(nums);
    cout << answer << " " << 0 << endl;

    nums = {1, 2};
    answer = solution.maxProfit(nums);
    cout << answer << " " << 1 << endl;

    nums = {2, 1};
    answer = solution.maxProfit(nums);
    cout << answer << " " << 0 << endl;

    return 0;
}