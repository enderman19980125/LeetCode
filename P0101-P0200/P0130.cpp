#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void solve(vector<vector<char>> &board) {
        if (board.empty() or board[0].empty()) return;
        int n = board.size(), m = board[0].size();
        int dx[] = {0, 0, -1, 1}, dy[] = {-1, 1, 0, 0};

        for (int i = 1; i < n - 1; ++i)
            for (int j = 1; j < m - 1; ++j)
                if (board[i][j] == 'O') {
                    vector<pair<int, int>> q;
                    q.emplace_back(i, j);
                    board[i][j] = 'o';
                    int k = 0;
                    bool is_border = false;

                    while (k < q.size()) {
                        auto point = q[k++];
                        int x = point.first, y = point.second;
                        for (int d = 0; d < 4; ++d) {
                            int xx = x + dx[d], yy = y + dy[d];
                            if (xx < 0 or yy < 0 or xx >= n or yy >= m or board[xx][yy] != 'O') continue;
                            if (xx == 0 or yy == 0 or xx == n - 1 or yy == m - 1) is_border = true;
                            q.emplace_back(pair<int, int>(xx, yy));
                            board[xx][yy] = 'o';
                        }
                    }

                    if (not is_border)
                        for (auto &point:q) board[point.first][point.second] = 'X';
                }

        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                if (board[i][j] == 'o') board[i][j] = 'O';
    }
};

string to_string(vector<vector<char>> &nums) {
    string s;
    for (auto &row:nums) {
        for (auto &element:row) s += element;
        s += "\n";
    }
    return s;
}

int main() {
    Solution solution = Solution();

    vector<vector<char>> nums;

    nums = {{'X', 'X', 'X', 'X'},
            {'X', 'O', 'O', 'X'},
            {'X', 'X', 'O', 'X'},
            {'X', 'O', 'X', 'X'}};
    cout << to_string(nums) << endl;
    solution.solve(nums);
    cout << to_string(nums) << endl;
    cout << "----------------" << endl;

    nums = {{'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O'},
            {'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'X'},
            {'O', 'X', 'O', 'X', 'O', 'O', 'O', 'O', 'X'},
            {'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O'},
            {'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'},
            {'X', 'X', 'O', 'O', 'X', 'O', 'X', 'O', 'X'},
            {'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O'},
            {'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O'},
            {'O', 'O', 'O', 'O', 'O', 'X', 'X', 'O', 'O'}};
    cout << to_string(nums) << endl;
    solution.solve(nums);
    cout << to_string(nums) << endl;
    cout << "----------------" << endl;

    nums = {{'X', 'X', 'X', 'X', 'X', 'X'},
            {'X', 'O', 'O', 'X', 'O', 'X'},
            {'X', 'O', 'O', 'X', 'O', 'X'},
            {'X', 'O', 'X', 'X', 'X', 'X'}};
    cout << to_string(nums) << endl;
    solution.solve(nums);
    cout << to_string(nums) << endl;
    cout << "----------------" << endl;

    nums = {{'X', 'X', 'X', 'X', 'X', 'X'},
            {'X', 'O', 'O', 'O', 'O', 'X'},
            {'X', 'O', 'O', 'X', 'O', 'X'},
            {'X', 'X', 'X', 'O', 'X', 'X'}};
    cout << to_string(nums) << endl;
    solution.solve(nums);
    cout << to_string(nums) << endl;
    cout << "----------------" << endl;

    nums = {{'X', 'X', 'X', 'X', 'X', 'X'},
            {'X', 'O', 'X', 'O', 'O', 'X'},
            {'O', 'O', 'O', 'X', 'O', 'X'},
            {'X', 'X', 'X', 'O', 'X', 'X'}};
    cout << to_string(nums) << endl;
    solution.solve(nums);
    cout << to_string(nums) << endl;
    cout << "----------------" << endl;

    nums = {};
    cout << to_string(nums) << endl;
    solution.solve(nums);
    cout << to_string(nums) << endl;
    cout << "----------------" << endl;

    nums = {{}};
    cout << to_string(nums) << endl;
    solution.solve(nums);
    cout << to_string(nums) << endl;
    cout << "----------------" << endl;

    nums = {{'X'}};
    cout << to_string(nums) << endl;
    solution.solve(nums);
    cout << to_string(nums) << endl;
    cout << "----------------" << endl;

    nums = {{'O'}};
    cout << to_string(nums) << endl;
    solution.solve(nums);
    cout << to_string(nums) << endl;
    cout << "----------------" << endl;

    return 0;
}