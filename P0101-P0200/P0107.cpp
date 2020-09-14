#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    explicit TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode *root) {
        vector<vector<int>> values;
        if (root == nullptr) return values;
        queue<TreeNode *> q[2];
        int k = 0;
        q[k].push(root);
        while (!q[k].empty()) {
            vector<int> level_values;
            while (!q[k].empty()) {
                TreeNode *node = q[k].front();
                q[k].pop();
                level_values.push_back(node->val);
                if (node->left) q[1 - k].push(node->left);
                if (node->right) q[1 - k].push(node->right);
            }
            k = 1 - k;
            values.push_back(level_values);
        }
        reverse(values.begin(), values.end());
        return values;
    }
};


TreeNode *vectorToTreeNode(vector<int> nodes) {
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
            if (nodes[k] == -1) {
                k++;
            } else {
                auto *left = new TreeNode(nodes[k++]);
                root->left = left;
                q.push(left);
            }
        }
        if (k < nodes.size()) {
            if (nodes[k] == -1) {
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

    vector<int> nodes;
    TreeNode *root_node;
    vector<vector<int>> answer;

    nodes = {3, 9, 20, -1, -1, 15, 7};
    root_node = vectorToTreeNode(nodes);
    answer = solution.levelOrderBottom(root_node);
    cout << doubleVectorToString(answer) << " " << "[[15, 7], [9, 20], [3]]" << endl;

    nodes = {};
    root_node = vectorToTreeNode(nodes);
    answer = solution.levelOrderBottom(root_node);
    cout << doubleVectorToString(answer) << " " << "[]" << endl;

    nodes = {1};
    root_node = vectorToTreeNode(nodes);
    answer = solution.levelOrderBottom(root_node);
    cout << doubleVectorToString(answer) << " " << "[[1]]" << endl;

    nodes = {1, 2, 3};
    root_node = vectorToTreeNode(nodes);
    answer = solution.levelOrderBottom(root_node);
    cout << doubleVectorToString(answer) << " " << "[[2, 3], [1]]" << endl;

    return 0;
}