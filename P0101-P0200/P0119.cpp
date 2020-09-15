#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> nums(rowIndex + 1, 1);
        for (int row = 2; row <= rowIndex; row++) {
            for (int i = row - 1; i >= 1; i--) nums[i] += nums[i - 1];
        }
        return nums;
    }
};

string vectorToString(vector<int> &array) {
    string s = "[";
    for (auto element:array) {
        s += to_string(element) + ", ";
    }
    s = (array.empty() ? s : s.substr(0, s.size() - 2)) + "]";
    return s;
}

int main() {
    Solution solution = Solution();

    vector<int> answer;

    answer = solution.getRow(5);
    cout << vectorToString(answer) << " " << "[1, 5, 10, 10, 5, 1]" << endl;

    answer = solution.getRow(0);
    cout << vectorToString(answer) << " " << "[1]" << endl;

    answer = solution.getRow(1);
    cout << vectorToString(answer) << " " << "[1, 1]" << endl;

    answer = solution.getRow(2);
    cout << vectorToString(answer) << " " << "[1, 2, 1]" << endl;

    answer = solution.getRow(3);
    cout << vectorToString(answer) << " " << "[1, 3, 3, 1]" << endl;

    answer = solution.getRow(4);
    cout << vectorToString(answer) << " " << "[1, 4, 6, 4, 1]" << endl;

    return 0;
}