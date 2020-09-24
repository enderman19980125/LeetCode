#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
        int n = gas.size();
        int rest[2 * n - 1];
        for (int i = 0; i < n; ++i) rest[i] = gas[i] - cost[i];
        for (int i = n; i < 2 * n - 1; ++i) rest[i] = rest[i % n];
        for (int i = 0; i < n; ++i) {
            int sumRest = 0;
            bool isSuccess = true;
            for (int d = 0; d < n; ++d) {
                sumRest += rest[i + d];
                if (sumRest < 0) {
                    isSuccess = false;
                    break;
                }
            }
            if (isSuccess) return i;
        }
        return -1;
    }
};

class SolutionN {
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
        int n = gas.size();
        int rest[2 * n - 1];
        for (int i = 0; i < n; ++i) rest[i] = gas[i] - cost[i];
        for (int i = n; i < 2 * n - 1; ++i) rest[i] = rest[i % n];
        int start = 0, cntTank = 0, sumTank = 0;
        for (int i = 0; i < n; ++i) {
            cntTank += rest[i];
            sumTank += rest[i];
            if (cntTank < 0) {
                start = i + 1;
                cntTank = 0;
            }
        }
        start = sumTank >= 0 ? start : -1;
        return start;
    }
};

int main() {
    Solution solution = Solution();

    vector<int> gas, cost;
    int answer;

    gas = {1, 2, 3, 4, 5};
    cost = {3, 4, 5, 1, 2};
    answer = solution.canCompleteCircuit(gas, cost);
    cout << answer << " " << 3 << endl;

    gas = {2, 3, 4};
    cost = {3, 4, 3};
    answer = solution.canCompleteCircuit(gas, cost);
    cout << answer << " " << -1 << endl;

    gas = {3, 1, 1};
    cost = {1, 2, 2};
    answer = solution.canCompleteCircuit(gas, cost);
    cout << answer << " " << 0 << endl;

    gas = {1, 2};
    cost = {2, 1};
    answer = solution.canCompleteCircuit(gas, cost);
    cout << answer << " " << 1 << endl;

    gas = {2};
    cost = {3};
    answer = solution.canCompleteCircuit(gas, cost);
    cout << answer << " " << -1 << endl;

    return 0;
}