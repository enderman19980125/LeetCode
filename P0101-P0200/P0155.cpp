#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class MinStack {
private:
    stack<int> minSt, St;
public:
    /** initialize your data structure here. */
    MinStack() = default;

    void push(int x) {
        St.push(x);
        if (minSt.empty() or x <= minSt.top()) minSt.push(x);
    }

    void pop() {
        if (St.top() == minSt.top()) minSt.pop();
        St.pop();
    }

    int top() {
        return St.top();
    }

    int getMin() {
        return minSt.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */

string test(vector<string> &operateList, vector<int> &numsList) {
    string s;
    MinStack minStack = MinStack();
    for (int i = 1; i < operateList.size(); ++i) {
        if (operateList[i] == "push") {
            minStack.push(numsList[i]);
            continue;
        }
        if (operateList[i] == "pop") {
            minStack.pop();
            continue;
        }
        if (operateList[i] == "top") {
            s.append(to_string(minStack.top()));
            s.append(",");
            continue;
        }
        if (operateList[i] == "getMin") {
            s.append(to_string(minStack.getMin()));
            s.append(",");
            continue;
        }
    }
    if (not s.empty()) s = s.substr(0, s.size() - 1);
    s = "[" + s + "]";
    return s;
}

int main() {
    vector<string> operateList;
    vector<int> numsList;
    string answer;

    operateList = {"MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"};
    numsList = {INT_MIN, -2, 0, -3, INT_MIN, INT_MIN, INT_MIN, INT_MIN};
    answer = test(operateList, numsList);
    cout << answer << " " << "[-3,0,-2]" << endl;

    operateList = {"MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"};
    numsList = {INT_MIN, -3, -2, -4, INT_MIN, INT_MIN, INT_MIN, INT_MIN};
    answer = test(operateList, numsList);
    cout << answer << " " << "[-4,-2,-3]" << endl;

    return 0;
}