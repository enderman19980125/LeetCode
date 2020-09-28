#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int> &numbers, int target) {
        unordered_map<int, int> m;
        int n = numbers.size();
        for (int j = 1; j < n; ++j) {
            if (numbers[0] + numbers[j] == target) return vector<int>{1, j + 1};
            if (numbers[0] + numbers[j] < target) m[numbers[j]] = j;
            if (numbers[0] + numbers[j] > target) break;
        }
        for (int i = 1; i < n; ++i) {
            int value = target - numbers[i];
            if (m.find(value) != m.end() and i < m[value])
                return vector<int>{i + 1, m[value] + 1};
        }
        return vector<int>{-1, -1};
    }
};

string to_string(const vector<int> &nums) {
    string s = "[";
    for (const int &num:nums) s += to_string(num) + ",";
    if (s.size() > 1) s = s.substr(0, s.size() - 1);
    s += "]";
    return s;
}

int main() {
    Solution solution = Solution();

    int target;
    vector<int> nums, answer;

    nums = {2, 7, 11, 15}, target = 9;
    answer = solution.twoSum(nums, target);
    cout << to_string(answer) << " " << "[1,2]" << endl;

    nums = {2, 3, 4}, target = 6;
    answer = solution.twoSum(nums, target);
    cout << to_string(answer) << " " << "[1,3]" << endl;

    nums = {-1, 0}, target = -1;
    answer = solution.twoSum(nums, target);
    cout << to_string(answer) << " " << "[1,2]" << endl;

    nums = {}, target = 8;
    answer = solution.twoSum(nums, target);
    cout << to_string(answer) << " " << "[-1,-1]" << endl;

    nums = {1}, target = 8;
    answer = solution.twoSum(nums, target);
    cout << to_string(answer) << " " << "[-1,-1]" << endl;

    nums = {2, 4}, target = 8;
    answer = solution.twoSum(nums, target);
    cout << to_string(answer) << " " << "[-1,-1]" << endl;

    nums = {4, 4}, target = 8;
    answer = solution.twoSum(nums, target);
    cout << to_string(answer) << " " << "[1,2]" << endl;

    nums = {2, 4, 4}, target = 8;
    answer = solution.twoSum(nums, target);
    cout << to_string(answer) << " " << "[2,3]" << endl;

    nums = {2, 3, 4, 5}, target = 8;
    answer = solution.twoSum(nums, target);
    cout << to_string(answer) << " " << "[2,4]" << endl;

    return 0;
}