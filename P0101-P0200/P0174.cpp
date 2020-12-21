#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int calculateMinimumHP(vector<vector<int>> &dungeon) {
        int n = dungeon.size(), m = dungeon[0].size();

        vector<vector<int>> hp(n, vector<int>(m, 0));
        hp[n - 1][m - 1] = max(1 - dungeon[n - 1][m - 1], 1);
        for (int j = m - 2; j >= 0; --j)
            hp[n - 1][j] = max(hp[n - 1][j + 1] - dungeon[n - 1][j], 1);
        for (int i = n - 2; i >= 0; --i)
            hp[i][m - 1] = max(hp[i + 1][m - 1] - dungeon[i][m - 1], 1);
        for (int i = n - 2; i >= 0; --i)
            for (int j = m - 2; j >= 0; --j) {
                int m0 = max(1 - dungeon[i][j], 1);
                int m1 = hp[i][j + 1] - dungeon[i][j];
                int m2 = hp[i + 1][j] - dungeon[i][j];
                hp[i][j] = min(m1, m2);
                if (hp[i][j] < m0) hp[i][j] = m0;
            }

        return hp[0][0];
    }
};

int main() {
    vector<vector<int>> nums;
    Solution solution = Solution();
    int answer;


    nums = {{-2, -3,  3},
            {-5, -10, 1},
            {10, 30,  -5}};
    answer = solution.calculateMinimumHP(nums);
    cout << answer << " " << 7 << endl;

    nums = {{-10, -10, -10, -10, -10},
            {-10, -1,  -10, -10, -10},
            {-10, -10, -1,  -10, -10}};
    answer = solution.calculateMinimumHP(nums);
    cout << answer << " " << 53 << endl;

    nums = {{-10, -10, 100, -10, -10},
            {-10, -1,  100, -10, -10},
            {-10, -10, 100, -10, -10}};
    answer = solution.calculateMinimumHP(nums);
    cout << answer << " " << 21 << endl;

    nums = {{0}};
    answer = solution.calculateMinimumHP(nums);
    cout << answer << " " << 1 << endl;

    nums = {{-5}};
    answer = solution.calculateMinimumHP(nums);
    cout << answer << " " << 6 << endl;

    nums = {{5}};
    answer = solution.calculateMinimumHP(nums);
    cout << answer << " " << 1 << endl;

    nums = {{5, -5}};
    answer = solution.calculateMinimumHP(nums);
    cout << answer << " " << 1 << endl;

    nums = {{-5, 5}};
    answer = solution.calculateMinimumHP(nums);
    cout << answer << " " << 6 << endl;

    nums = {{5},
            {-5}};
    answer = solution.calculateMinimumHP(nums);
    cout << answer << " " << 1 << endl;

    nums = {{-5},
            {5}};
    answer = solution.calculateMinimumHP(nums);
    cout << answer << " " << 6 << endl;

    return 0;
}