#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int numIslands(vector<vector<char>> &grid) {
        int dx[] = {0, 0, -1, 1}, dy[] = {-1, 1, 0, 0};
        int n = grid.size(), m = grid[0].size(), num = 0;

        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                if (grid[i][j] == '1') {
                    num++;
                    grid[i][j] = '0';
                    queue<pair<int, int>> q;
                    q.emplace(pair<int, int>{i, j});
                    while (not q.empty()) {
                        auto xy = q.front();
                        int x = xy.first, y = xy.second;
                        q.pop();
                        grid[x][y] = '0';
                        for (int k = 0; k < 4; ++k) {
                            int xx = x + dx[k], yy = y + dy[k];
                            if (xx < 0 or xx >= n or yy < 0 or yy >= m or grid[xx][yy] == '0') continue;
                            grid[xx][yy] = '0';
                            q.emplace(pair<int, int>{xx, yy});
                        }
                    }
                }

        return num;
    }
};

int main() {
    Solution solution = Solution();

    vector<vector<char>> grid;
    int answer;

    grid = {{'1', '1', '1', '1', '0'},
            {'1', '1', '0', '1', '0'},
            {'1', '1', '0', '0', '0'},
            {'0', '0', '0', '0', '0'},
    };
    answer = solution.numIslands(grid);
    cout << answer << " " << 1 << endl;

    grid = {{'1', '1', '0', '0', '0'},
            {'1', '1', '0', '0', '0'},
            {'0', '0', '1', '0', '0'},
            {'0', '0', '0', '1', '1'},
    };
    answer = solution.numIslands(grid);
    cout << answer << " " << 3 << endl;

    grid = {{'0'}};
    answer = solution.numIslands(grid);
    cout << answer << " " << 0 << endl;

    grid = {{'1'}};
    answer = solution.numIslands(grid);
    cout << answer << " " << 1 << endl;

    grid = {{'1', '0', '1', '0', '1'},
            {'1', '1', '0', '1', '1'},
    };
    answer = solution.numIslands(grid);
    cout << answer << " " << 3 << endl;

    grid = {{'1', '0', '1', '0', '1'},
            {'0', '1', '0', '1', '0'},
    };
    answer = solution.numIslands(grid);
    cout << answer << " " << 5 << endl;

    return 0;
}