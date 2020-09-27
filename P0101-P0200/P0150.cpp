#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    int evalRPN(vector<string> &tokens) {
        if (tokens.empty()) return 0;
        size_t k = 0, n = tokens.size();
        stack<int> st;
        while (k < n) {
            if (tokens[k] == "+" or tokens[k] == "-" or tokens[k] == "*" or tokens[k] == "/") {
                int b = st.top();
                st.pop();
                int a = st.top();
                st.pop();
                if (tokens[k] == "+") a += b;
                if (tokens[k] == "-") a -= b;
                if (tokens[k] == "*") a *= b;
                if (tokens[k] == "/") a /= b;
                st.emplace(a);
            } else {
                st.emplace(stoi(tokens[k]));
            }
            k++;
        }
        return st.top();
    }
};

int main() {
    Solution solution = Solution();

    vector<string> expression;
    int answer;

    expression = {"2", "1", "+", "3", "*"};
    answer = solution.evalRPN(expression);
    cout << answer << " " << 9 << endl;

    expression = {"4", "13", "5", "/", "+"};
    answer = solution.evalRPN(expression);
    cout << answer << " " << 6 << endl;

    expression = {"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"};
    answer = solution.evalRPN(expression);
    cout << answer << " " << 22 << endl;

    expression = {};
    answer = solution.evalRPN(expression);
    cout << answer << " " << 0 << endl;

    expression = {"-3", "2", "/"};
    answer = solution.evalRPN(expression);
    cout << answer << " " << -1 << endl;

    expression = {"3", "-2", "/"};
    answer = solution.evalRPN(expression);
    cout << answer << " " << -1 << endl;

    return 0;
}