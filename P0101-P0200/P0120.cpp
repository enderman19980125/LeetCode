#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int minimumTotal(vector<vector<int>> &triangle) {
        if (triangle.empty()) return 0;
        int numRows = triangle.size();
        for (int i = numRows - 2; i >= 0; i--)
            for (int j = 0; j <= i; j++)
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1]);
        return triangle[0][0];
    }
};

int main() {
    Solution solution = Solution();

    vector<vector<int>> nums;
    int answer;

    nums = {{2},
            {3, 4},
            {6, 5, 7},
            {4, 1, 8, 3}};
    answer = solution.minimumTotal(nums);
    cout << answer << " " << 11 << endl;

    nums = {};
    answer = solution.minimumTotal(nums);
    cout << answer << " " << 0 << endl;

    nums = {{2}};
    answer = solution.minimumTotal(nums);
    cout << answer << " " << 2 << endl;

    nums = {{2},
            {3, 4}};
    answer = solution.minimumTotal(nums);
    cout << answer << " " << 5 << endl;

    nums = {{2},
            {3, 4},
            {6, 5, 7}};
    answer = solution.minimumTotal(nums);
    cout << answer << " " << 10 << endl;

    return 0;
}