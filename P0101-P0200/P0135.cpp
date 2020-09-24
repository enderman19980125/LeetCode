#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int candy(vector<int> &ratings) {
        if (ratings.empty()) return 0;
        int n = ratings.size(), candy[n], j;
        for (int i = 0; i < n; ++i) candy[i] = 1;

        for (int i = 0; i < n; ++i) {
            if (1 <= i and i <= n - 2 and ratings[i - 1] < ratings[i] and ratings[i] < ratings[i + 1]) continue;
            if (1 <= i and i <= n - 2 and ratings[i - 1] > ratings[i] and ratings[i] > ratings[i + 1]) continue;
            j = i;
            while (j - 1 >= 0 and ratings[j - 1] > ratings[j]) {
                candy[j - 1] = max(candy[j - 1], candy[j] + 1);
                j--;
            }
            j = i;
            while (j + 1 < n and ratings[j + 1] > ratings[j]) {
                candy[j + 1] = max(candy[j + 1], candy[j] + 1);
                j++;
            }
        }

        int sumCandy = 0;
        for (int c:candy) sumCandy += c;
        return sumCandy;
    }
};

int main() {
    Solution solution = Solution();

    vector<int> nums;
    int answer;

    nums = {1, 0, 2};
    answer = solution.candy(nums);
    cout << answer << " " << 5 << endl;

    nums = {1, 2, 2};
    answer = solution.candy(nums);
    cout << answer << " " << 4 << endl;

    nums = {};
    answer = solution.candy(nums);
    cout << answer << " " << 0 << endl;

    nums = {1};
    answer = solution.candy(nums);
    cout << answer << " " << 1 << endl;

    nums = {1, 2, 1};
    answer = solution.candy(nums);
    cout << answer << " " << 4 << endl;

    nums = {1, 2, 2, 3};
    answer = solution.candy(nums);
    cout << answer << " " << 6 << endl;

    nums = {3, 2, 2, 1};
    answer = solution.candy(nums);
    cout << answer << " " << 6 << endl;

    nums = {2, 1, 2, 2, 3, 1};
    answer = solution.candy(nums);
    cout << answer << " " << 9 << endl;

    nums = {1, 1, 2, 2, 3, 3, 4, 4, 1, 1};
    answer = solution.candy(nums);
    cout << answer << " " << 14 << endl;

    return 0;
}