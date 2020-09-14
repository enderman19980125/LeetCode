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
private:
    vector<TreeNode *> nodes;

    void preorderTraversal(TreeNode *&root) {
        if (root == nullptr) return;
        this->nodes.push_back(root);
        this->preorderTraversal(root->left);
        this->preorderTraversal(root->right);
    }

public:
    void flatten(TreeNode *root) {
        nodes.clear();
        this->preorderTraversal(root);
        for (int i = 1; i < this->nodes.size(); i++) {
            nodes[i - 1]->left = nullptr;
            nodes[i - 1]->right = nodes[i];
        }
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

string treeNodeToFlattenString(TreeNode *root) {
    vector<int> output;
    while (root) {
        output.push_back(root->val);
        root = root->right;
    }
    string output_string;
    for (auto value:output) {
        output_string += to_string(value) + ", ";
    }
    return "[" + output_string.substr(0, output_string.length() - 2) + "]";
}

int main() {
    Solution solution = Solution();

    vector<int> nums;
    vector<vector<int>> answer;
    TreeNode *root;

    nums = {1, 2, 5, 3, 4, -1, 6};
    root = vectorToTreeNode(nums);
    solution.flatten(root);
    cout << treeNodeToFlattenString(root) << " " << "[1, 2, 3, 4, 5, 6]" << endl;

    nums = {};
    root = vectorToTreeNode(nums);
    solution.flatten(root);
    cout << treeNodeToFlattenString(root) << " " << "[]" << endl;

    nums = {1};
    root = vectorToTreeNode(nums);
    solution.flatten(root);
    cout << treeNodeToFlattenString(root) << " " << "[1]" << endl;

    nums = {1, 2, 3};
    root = vectorToTreeNode(nums);
    solution.flatten(root);
    cout << treeNodeToFlattenString(root) << " " << "[1, 2, 3]" << endl;

    nums = {1, 2, 3, -1, 4};
    root = vectorToTreeNode(nums);
    solution.flatten(root);
    cout << treeNodeToFlattenString(root) << " " << "[1, 2, 4, 3]" << endl;

    return 0;
}