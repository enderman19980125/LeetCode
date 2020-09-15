#include <iostream>
#include <vector>

using namespace std;

class Solution {
private:
    void generateLevel(int numRemain, vector<vector<int>> &nums) {
        vector<int> levelNums = {1};
        if (!nums.empty()) {
            vector<int> preLevelNums = nums[nums.size() - 1];
            for (int i = 1; i < preLevelNums.size(); i++)
                levelNums.push_back(preLevelNums[i - 1] + preLevelNums[i]);
        }
        levelNums.push_back(1);
        nums.push_back(levelNums);
        if (numRemain > 0) this->generateLevel(numRemain - 1, nums);
    }

public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> nums;
        if (numRows == 0) return nums;
        nums.push_back(vector<int>{1});
        if (numRows == 1) return nums;
        this->generateLevel(numRows - 2, nums);
        return nums;
    }
};

string doubleVectorToString(const vector<vector<int>> &array) {
    string s = "[";
    for (auto &row: array) {
        s += "[";
        for (auto element:row) {
            s += to_string(element) + ", ";
        }
        s = (row.empty() ? s : s.substr(0, s.size() - 2)) + "], ";
    }
    s = (array.empty() ? s : s.substr(0, s.size() - 2)) + "]";
    return s;
}

int main() {
    Solution solution = Solution();

    vector<vector<int>> answer;

    answer = solution.generate(5);
    cout << doubleVectorToString(answer) << " " << "[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]" << endl;

    answer = solution.generate(0);
    cout << doubleVectorToString(answer) << " " << "[]" << endl;

    answer = solution.generate(1);
    cout << doubleVectorToString(answer) << " " << "[[1]]" << endl;

    answer = solution.generate(2);
    cout << doubleVectorToString(answer) << " " << "[[1], [1, 1]]" << endl;

    answer = solution.generate(3);
    cout << doubleVectorToString(answer) << " " << "[[1], [1, 1], [1, 2, 1]]" << endl;

    answer = solution.generate(4);
    cout << doubleVectorToString(answer) << " " << "[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]" << endl;

    return 0;
}