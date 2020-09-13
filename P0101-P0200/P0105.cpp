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
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
        if (preorder.empty()) return nullptr;
        auto *root = new TreeNode(preorder[0]);
        auto iterator_root = find(inorder.begin(), inorder.end(), root->val);
        vector<int> left_inorder(inorder.begin(), iterator_root);
        vector<int> right_inorder(iterator_root + 1, inorder.end());
        vector<int> left_preorder(preorder.begin() + 1, preorder.begin() + 1 + left_inorder.size());
        vector<int> right_preorder(preorder.begin() + 1 + left_inorder.size(), preorder.end());
        root->left = this->buildTree(left_preorder, left_inorder);
        root->right = this->buildTree(right_preorder, right_inorder);
        return root;
    }
};

string treeNodeToString(TreeNode *root) {
    if (root == nullptr) return "[]";
    vector<int> output;
    queue<TreeNode *> q;
    q.push(root);
    while (!q.empty()) {
        TreeNode *node = q.front();
        q.pop();
        if (node == nullptr) {
            output.push_back(-1);
            continue;
        }
        output.push_back(node->val);
        q.push(node->left);
        q.push(node->right);
    }
    while (*output.rbegin() == -1) {
        output.pop_back();
    }
    string output_string;
    for (auto value:output) {
        output_string += to_string(value) + ", ";
    }
    return "[" + output_string.substr(0, output_string.length() - 2) + "]";
}

int main() {
    Solution solution = Solution();

    vector<int> preorder, inorder;
    TreeNode *answer;

    preorder = {3, 9, 20, 15, 7};
    inorder = {9, 3, 15, 20, 7};
    answer = solution.buildTree(preorder, inorder);
    cout << treeNodeToString(answer) << " " << "[3, 9, 20, -1, -1, 15, 7]" << endl;

    preorder = {};
    inorder = {};
    answer = solution.buildTree(preorder, inorder);
    cout << treeNodeToString(answer) << " " << "[]" << endl;

    preorder = {1};
    inorder = {1};
    answer = solution.buildTree(preorder, inorder);
    cout << treeNodeToString(answer) << " " << "[1]" << endl;

    preorder = {1, 2, 3};
    inorder = {2, 1, 3};
    answer = solution.buildTree(preorder, inorder);
    cout << treeNodeToString(answer) << " " << "[1, 2, 3]" << endl;

    return 0;
}