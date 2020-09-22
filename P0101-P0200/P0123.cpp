#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int> &prices) {
        if (prices.empty()) return 0;
        int n = prices.size();

        int maxLeft[n], maxRight[n];

        int minPrice = prices[0], maxProfit = 0;
        for (int i = 0; i < n; ++i) {
            maxProfit = max(maxProfit, prices[i] - minPrice);
            minPrice = min(minPrice, prices[i]);
            maxLeft[i] = maxProfit;
        }

        int maxPrice = prices[n - 1];
        maxProfit = 0;
        for (int i = n - 1; i >= 0; --i) {
            maxProfit = max(maxProfit, maxPrice - prices[i]);
            maxPrice = max(maxPrice, prices[i]);
            maxRight[i] = maxProfit;
        }

        maxProfit = maxLeft[n - 1];
        for (int i = 1; i <= n - 2; ++i)
            maxProfit = max(maxProfit, maxLeft[i] + maxRight[i]);

        return maxProfit;
    }
};

int main() {
    Solution solution = Solution();

    vector<int> nums;
    int answer;

    nums = {3, 3, 5, 0, 0, 3, 1, 4};
    answer = solution.maxProfit(nums);
    cout << answer << " " << 6 << endl;

    nums = {1, 2, 3, 4, 5};
    answer = solution.maxProfit(nums);
    cout << answer << " " << 4 << endl;

    nums = {7, 6, 4, 3, 1};
    answer = solution.maxProfit(nums);
    cout << answer << " " << 0 << endl;

    nums = {1};
    answer = solution.maxProfit(nums);
    cout << answer << " " << 0 << endl;

    nums = {1, 2, 4, 2, 5, 7, 2, 4, 9, 0};
    answer = solution.maxProfit(nums);
    cout << answer << " " << 13 << endl;

    nums = {};
    answer = solution.maxProfit(nums);
    cout << answer << " " << 0 << endl;

    nums = {1, 2};
    answer = solution.maxProfit(nums);
    cout << answer << " " << 1 << endl;

    nums = {2, 1};
    answer = solution.maxProfit(nums);
    cout << answer << " " << 0 << endl;

    nums = {0, 1, 2, 1, 2, 1, 2, 10};
    answer = solution.maxProfit(nums);
    cout << answer << " " << 11 << endl;

    return 0;
}