#include <iostream>
#include <memory.h>
#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(int k, vector<int> &prices) {
        if (prices.size() <= 1) return 0;

        vector<pair<int, int>> stages;
        int l = 0, r = 0;
        while (r != prices.size() - 1) {
            while (r + 1 < prices.size() and prices[r] <= prices[r + 1]) ++r;
            if (prices[l] < prices[r]) stages.emplace_back(pair<int, int>{prices[l], prices[r]});
            while (r + 1 < prices.size() and prices[r] >= prices[r + 1]) ++r;
            l = r;
        }

        if (stages.empty()) return 0;

        int n = stages.size(), maxProfitOnce[n][n];
        memset(maxProfitOnce, 0, sizeof(maxProfitOnce));
        for (int i = 0; i < n; ++i) maxProfitOnce[i][i] = stages[i].second - stages[i].first;
        for (int d = 2; d <= n; ++d)
            for (int i = 0, j = d - 1; j < n; ++i, ++j) {
                maxProfitOnce[i][j] = max(maxProfitOnce[i][j - 1], maxProfitOnce[i + 1][j]);
                maxProfitOnce[i][j] = max(maxProfitOnce[i][j], stages[j].second - stages[i].first);
            }


        int dp[n][n + 1];
        memset(dp, 0, sizeof(dp));
        dp[0][1] = maxProfitOnce[0][0];
        for (int i = 1; i < n; ++i)
            for (int c = 1; c <= i + 1; ++c) {
                if (c == 1) dp[i][c] = maxProfitOnce[0][i];
                dp[i][c] = max(dp[i][c], dp[i - 1][c]);
                for (int j = 0; j < i; ++j) dp[i][c] = max(dp[i][c], dp[j][c - 1] + maxProfitOnce[j + 1][i]);
            }

        if (k > n) return dp[n - 1][n]; else return dp[n - 1][k];
    }
};

int main() {
    int k, answer;
    vector<int> prices;
    Solution solution = Solution();

    k = 2;
    prices = {2, 4, 1};
    answer = solution.maxProfit(k, prices);
    cout << answer << " " << 2 << endl;

    k = 2;
    prices = {3, 2, 6, 5, 0, 3};
    answer = solution.maxProfit(k, prices);
    cout << answer << " " << 7 << endl;

    k = 2;
    prices = {3, 2, 1, 3, 2, 1};
    answer = solution.maxProfit(k, prices);
    cout << answer << " " << 2 << endl;

    k = 2;
    prices = {3, 2, 1, 4, 2, 3, 2, 1};
    answer = solution.maxProfit(k, prices);
    cout << answer << " " << 4 << endl;

    k = 1;
    prices = {3, 2, 1, 4, 2, 3, 2, 1};
    answer = solution.maxProfit(k, prices);
    cout << answer << " " << 3 << endl;

    k = 1;
    prices = {3, 2, 1, 4, 2, 5, 3, 6, 5, 4};
    answer = solution.maxProfit(k, prices);
    cout << answer << " " << 5 << endl;

    k = 2;
    prices = {3, 2, 1, 4, 2, 5, 3, 6, 5, 4};
    answer = solution.maxProfit(k, prices);
    cout << answer << " " << 7 << endl;

    k = 3;
    prices = {3, 2, 1, 4, 2, 5, 3, 6, 5, 4};
    answer = solution.maxProfit(k, prices);
    cout << answer << " " << 9 << endl;

    k = 4;
    prices = {3, 2, 1, 4, 2, 5, 3, 6, 5, 4};
    answer = solution.maxProfit(k, prices);
    cout << answer << " " << 9 << endl;

    k = 5;
    prices = {3, 2, 1, 4, 2, 5, 3, 6, 5, 4};
    answer = solution.maxProfit(k, prices);
    cout << answer << " " << 9 << endl;

    k = 5;
    prices = {};
    answer = solution.maxProfit(k, prices);
    cout << answer << " " << 0 << endl;

    k = 5;
    prices = {1};
    answer = solution.maxProfit(k, prices);
    cout << answer << " " << 0 << endl;

    k = 5;
    prices = {2, 1};
    answer = solution.maxProfit(k, prices);
    cout << answer << " " << 0 << endl;

    k = 5;
    prices = {1, 2};
    answer = solution.maxProfit(k, prices);
    cout << answer << " " << 1 << endl;

    return 0;
}