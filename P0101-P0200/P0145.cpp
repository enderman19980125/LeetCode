#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode() : val(0), left(nullptr), right(nullptr) {}

    explicit TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}

    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<int> postorderTraversal(TreeNode *root) {
        vector<int> ans;
        if (root == nullptr) return ans;
        stack<TreeNode *> st;
        st.emplace(root);
        while (not st.empty()) {
            TreeNode *node = st.top();
            st.pop();
            ans.emplace_back(node->val);
            if (node->left) st.emplace(node->left);
            if (node->right) st.emplace(node->right);
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};

TreeNode *vectorToTreeNode(const vector<int> &nodes) {
    if (nodes.empty()) {
        return nullptr;
    }
    queue<TreeNode *> q;
    auto *root_node = new TreeNode(nodes[0]);
    q.push(root_node);
    int k = 1;
    while (k < nodes.size()) {
        TreeNode *root = q.front();
        q.pop();
        if (k < nodes.size()) {
            if (nodes[k] == INT_MIN) {
                k++;
            } else {
                auto *left = new TreeNode(nodes[k++]);
                root->left = left;
                q.push(left);
            }
        }
        if (k < nodes.size()) {
            if (nodes[k] == INT_MIN) {
                k++;
            } else {
                auto *right = new TreeNode(nodes[k++]);
                root->right = right;
                q.push(right);
            }
        }
    }
    return root_node;
}

string to_string(const vector<int> &nums) {
    string s = "[";
    for (const int &num: nums) s += to_string(num) + ",";
    if (not nums.empty()) s = s.substr(0, s.size() - 1);
    s += "]";
    return s;
}

int main() {
    Solution solution = Solution();

    TreeNode *root;
    vector<int> answer;

    root = vectorToTreeNode(vector<int>{1, INT_MIN, 2, 3});
    answer = solution.postorderTraversal(root);
    cout << to_string(answer) << " " << "[3,2,1]" << endl;

    root = vectorToTreeNode(vector<int>{});
    answer = solution.postorderTraversal(root);
    cout << to_string(answer) << " " << "[]" << endl;

    root = vectorToTreeNode(vector<int>{1});
    answer = solution.postorderTraversal(root);
    cout << to_string(answer) << " " << "[1]" << endl;

    root = vectorToTreeNode(vector<int>{1, 2});
    answer = solution.postorderTraversal(root);
    cout << to_string(answer) << " " << "[2,1]" << endl;

    root = vectorToTreeNode(vector<int>{1, INT_MIN, 2});
    answer = solution.postorderTraversal(root);
    cout << to_string(answer) << " " << "[2,1]" << endl;

    root = vectorToTreeNode(vector<int>{1, 2, 3, 4, INT_MIN, INT_MIN, 5});
    answer = solution.postorderTraversal(root);
    cout << to_string(answer) << " " << "[4,2,5,3,1]" << endl;

    return 0;
}