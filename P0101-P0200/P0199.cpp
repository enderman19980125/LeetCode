#include <iostream>
#include <vector>
#include <queue>

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
    vector<int> rightSideView(TreeNode *root) {
        vector<int> view;
        queue<pair<TreeNode *, int>> q;
        q.emplace(pair<TreeNode *, int>{root, 0});
        if (root == nullptr) return view;

        while (not q.empty()) {
            auto node_depth = q.front();
            auto node = node_depth.first;
            auto depth = node_depth.second;
            q.pop();
            if (depth + 1 > view.size()) view.resize(depth + 1);
            view[depth] = node->val;
            if (node->left) q.emplace(pair<TreeNode *, int>{node->left, depth + 1});
            if (node->right) q.emplace(pair<TreeNode *, int>{node->right, depth + 1});
        }

        return view;
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

string to_string(vector<int> &s) {
    string ans = "[";
    for (auto &i:s) ans.append(to_string(i) + ",");
    if (not s.empty()) ans = ans.substr(0, ans.size() - 1);
    ans.append("]");
    return ans;
}

int main() {
    Solution solution = Solution();

    vector<int> nums, answer;
    TreeNode *root;

    nums = {1, 2, 3, INT_MIN, 5, INT_MIN, 4};
    root = vectorToTreeNode(nums);
    answer = solution.rightSideView(root);
    cout << to_string(answer) << " " << "[1,3,4]" << endl;

    nums = {};
    root = vectorToTreeNode(nums);
    answer = solution.rightSideView(root);
    cout << to_string(answer) << " " << "[]" << endl;

    nums = {1};
    root = vectorToTreeNode(nums);
    answer = solution.rightSideView(root);
    cout << to_string(answer) << " " << "[1]" << endl;

    nums = {1, 2};
    root = vectorToTreeNode(nums);
    answer = solution.rightSideView(root);
    cout << to_string(answer) << " " << "[1,2]" << endl;

    nums = {1, 2, 3};
    root = vectorToTreeNode(nums);
    answer = solution.rightSideView(root);
    cout << to_string(answer) << " " << "[1,3]" << endl;

    nums = {1, 2, 3, 4, INT_MIN};
    root = vectorToTreeNode(nums);
    answer = solution.rightSideView(root);
    cout << to_string(answer) << " " << "[1,3,4]" << endl;

    return 0;
}