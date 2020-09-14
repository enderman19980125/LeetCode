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
    TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder) {
        if (inorder.empty()) return nullptr;
        auto *root = new TreeNode(*postorder.rbegin());
        if (inorder.size() == 1) return root;
        auto inorder_split = find(inorder.begin(), inorder.end(), root->val);
        vector<int> left_inorder(inorder.begin(), inorder_split);
        vector<int> right_inorder(inorder_split + 1, inorder.end());
        vector<int> left_postorder(postorder.begin(), postorder.begin() + left_inorder.size());
        vector<int> right_postorder(postorder.begin() + left_inorder.size(), postorder.end() - 1);
        root->left = this->buildTree(left_inorder, left_postorder);
        root->right = this->buildTree(right_inorder, right_postorder);
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

    vector<int> inorder, postorder;
    TreeNode *answer;

    inorder = {9, 3, 15, 20, 7};
    postorder = {9, 15, 7, 20, 3};
    answer = solution.buildTree(inorder, postorder);
    cout << treeNodeToString(answer) << " " << "[3, 9, 20, -1, -1, 15, 7]" << endl;

    inorder = {};
    postorder = {};
    answer = solution.buildTree(inorder, postorder);
    cout << treeNodeToString(answer) << " " << "[]" << endl;

    inorder = {2, 1};
    postorder = {2, 1};
    answer = solution.buildTree(inorder, postorder);
    cout << treeNodeToString(answer) << " " << "[1, 2]" << endl;

    inorder = {2, 1, 3};
    postorder = {2, 3, 1};
    answer = solution.buildTree(inorder, postorder);
    cout << treeNodeToString(answer) << " " << "[1, 2, 3]" << endl;

    return 0;
}