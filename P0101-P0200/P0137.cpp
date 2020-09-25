#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int> &nums) {
        unordered_map<int, int> m;
        for (int &num:nums) {
            if (m.find(num) == m.end())
                m[num] = 1;
            else
                m[num] += 1;
        }
        for (auto item:m) if (item.second == 1) return item.first;
        return 0;
    }
};

class SolutionBit {
public:
    int singleNumber(vector<int> &nums) {
        int once = 0, twice = 0;
        for (int &num:nums) {
            once = ~twice & (once ^ num);
            twice = ~once & (twice ^ num);
        }
        return once;
    }
};

int main() {
    Solution solution = Solution();

    vector<int> nums;
    int answer;

    nums = {2, 2, 3, 2};
    answer = solution.singleNumber(nums);
    cout << answer << " " << 3 << endl;

    nums = {0, 1, 0, 1, 0, 1, 99};
    answer = solution.singleNumber(nums);
    cout << answer << " " << 99 << endl;

    return 0;
}