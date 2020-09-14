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
    bool hasPathSum(TreeNode *root, int sum) {
        if (root == nullptr) return false;
        if (root->left == nullptr and root->right == nullptr) {
            return root->val == sum;
        }
        return this->hasPathSum(root->left, sum - root->val) or this->hasPathSum(root->right, sum - root->val);
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

int main() {
    Solution solution = Solution();

    vector<int> nums;
    bool answer;

    nums = {5, 4, 8, 11, -1, 13, 4, 7, 2, -1, -1, -1, 1};
    answer = solution.hasPathSum(vectorToTreeNode(nums), 22);
    cout << answer << " " << "1" << endl;

    nums = {};
    answer = solution.hasPathSum(vectorToTreeNode(nums), 0);
    cout << answer << " " << "0" << endl;

    nums = {1};
    answer = solution.hasPathSum(vectorToTreeNode(nums), 1);
    cout << answer << " " << "1" << endl;

    nums = {1};
    answer = solution.hasPathSum(vectorToTreeNode(nums), 2);
    cout << answer << " " << "0" << endl;

    nums = {5, 4, 8, 11, -1, 13, 4, 7, 2, -1, -1, -1, 1};
    answer = solution.hasPathSum(vectorToTreeNode(nums), 18);
    cout << answer << " " << "1" << endl;

    nums = {5, 4, 8, 11, -1, 13, 4, 7, 2, -1, -1, -1, 1};
    answer = solution.hasPathSum(vectorToTreeNode(nums), 26);
    cout << answer << " " << "1" << endl;

    nums = {5, 4, 8, 11, -1, 13, 4, 7, 2, -1, -1, -1, 1};
    answer = solution.hasPathSum(vectorToTreeNode(nums), 17);
    cout << answer << " " << "0" << endl;

    return 0;
}