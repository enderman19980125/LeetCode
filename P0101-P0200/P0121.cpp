#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int> &prices) {
        if (prices.empty()) return 0;
        int maxProfit = 0, minPrice = prices[0];
        for (auto price:prices) {
            maxProfit = max(maxProfit, price - minPrice);
            minPrice = min(minPrice, price);
        }
        return maxProfit;
    }
};

int main() {
    Solution solution = Solution();

    vector<int> nums;
    int answer;

    nums = {7, 1, 5, 3, 6, 4};
    answer = solution.maxProfit(nums);
    cout << answer << " " << 5 << endl;

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

    nums = {3, 1, 5, 3, 8, 6};
    answer = solution.maxProfit(nums);
    cout << answer << " " << 7 << endl;

    return 0;
}