#include <iostream>
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
    vector<vector<int>> zigzagLevelOrder(TreeNode *root) {
        vector<vector<int>> level_values;
        vector<TreeNode *> level_nodes[2];

        if (root == nullptr) {
            return level_values;
        }

        int k = 0;
        level_nodes[0].push_back(root);
        while (!level_nodes[k].empty()) {
            vector<int> values;
            level_nodes[1 - k].clear();
            if (k == 0) {
                for (auto &node : level_nodes[k])
                    values.push_back(node->val);
            } else {
                for (auto node = level_nodes[k].rbegin(); node != level_nodes[k].rend(); node++)
                    values.push_back((*node)->val);
            }
            for (auto &node:level_nodes[k]) {
                if (node->left) level_nodes[1 - k].push_back(node->left);
                if (node->right) level_nodes[1 - k].push_back(node->right);
            }
            level_nodes[k].clear();
            level_values.push_back(values);
            k = 1 - k;
        }
        return level_values;
    }
};


TreeNode *toTree(vector<int> nodes) {
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

string toString(const vector<vector<int>> &array) {
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
    root_node = toTree(nodes);
    answer = solution.zigzagLevelOrder(root_node);
    cout << toString(answer) << " " << "[[3], [20, 9], [15, 7]]" << endl;

    nodes = {};
    root_node = toTree(nodes);
    answer = solution.zigzagLevelOrder(root_node);
    cout << toString(answer) << " " << "[]" << endl;

    nodes = {1};
    root_node = toTree(nodes);
    answer = solution.zigzagLevelOrder(root_node);
    cout << toString(answer) << " " << "[[1]]" << endl;

    nodes = {1, -1, 2, 3, -1, 4, 5};
    root_node = toTree(nodes);
    answer = solution.zigzagLevelOrder(root_node);
    cout << toString(answer) << " " << "[[1], [2], [3], [5, 4]]" << endl;


    return 0;
}