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
private:
    int maxPath = INT_MIN;

    int maxPathStartFromNode(TreeNode *root) {
        if (root == nullptr) return 0;
        this->maxPath = max(this->maxPath, root->val);
        if (root->left == nullptr and root->right == nullptr) return root->val;
        int maxPathStartFromLeft = maxPathStartFromNode(root->left);
        int maxPathStartFromRight = maxPathStartFromNode(root->right);
        this->maxPath = max(this->maxPath, maxPathStartFromLeft + root->val);
        this->maxPath = max(this->maxPath, maxPathStartFromRight + root->val);
        this->maxPath = max(this->maxPath, maxPathStartFromLeft + maxPathStartFromRight + root->val);
        return root->val + max(0, max(maxPathStartFromLeft, maxPathStartFromRight));
    }

public:
    int maxPathSum(TreeNode *root) {
        this->maxPath = INT_MIN;
        int rootSum = this->maxPathStartFromNode(root);
        this->maxPath = max(this->maxPath, rootSum);
        return this->maxPath;
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

int main() {
    Solution solution = Solution();

    vector<int> nums;
    TreeNode *root;
    int answer;

    nums = {1, 2, 3};
    root = vectorToTreeNode(nums);
    answer = solution.maxPathSum(root);
    cout << answer << " " << 6 << endl;

    nums = {-10, 9, 20, INT_MIN, INT_MIN, 15, 7};
    root = vectorToTreeNode(nums);
    answer = solution.maxPathSum(root);
    cout << answer << " " << 42 << endl;

    nums = {0};
    root = vectorToTreeNode(nums);
    answer = solution.maxPathSum(root);
    cout << answer << " " << 0 << endl;

    nums = {-2, 1};
    root = vectorToTreeNode(nums);
    answer = solution.maxPathSum(root);
    cout << answer << " " << 1 << endl;

    nums = {-2, -1};
    root = vectorToTreeNode(nums);
    answer = solution.maxPathSum(root);
    cout << answer << " " << -1 << endl;

    nums = {9, 6, -3, INT_MIN, INT_MIN, -6, 2, INT_MIN, INT_MIN, 2, INT_MIN, -6, -6, -6};
    root = vectorToTreeNode(nums);
    answer = solution.maxPathSum(root);
    cout << answer << " " << 16 << endl;

    nums = {-10, 9, 20, INT_MIN, INT_MIN, INT_MIN, 7};
    root = vectorToTreeNode(nums);
    answer = solution.maxPathSum(root);
    cout << answer << " " << 27 << endl;

    nums = {-8, 9, 20, INT_MIN, INT_MIN, INT_MIN, 7};
    root = vectorToTreeNode(nums);
    answer = solution.maxPathSum(root);
    cout << answer << " " << 28 << endl;

    return 0;
}