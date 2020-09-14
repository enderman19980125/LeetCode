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
    int minDepth(TreeNode *root) {
        if (root == nullptr) return 0;
        if (root->left == nullptr and root->right == nullptr) return 1;
        if (root->left == nullptr) return 1 + this->minDepth(root->right);
        if (root->right == nullptr) return 1 + this->minDepth(root->left);
        return 1 + min(this->minDepth(root->left), this->minDepth(root->right));
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
    int answer;

    nums = {3, 9, 20, -1, -1, 15, 7};
    answer = solution.minDepth(vectorToTreeNode(nums));
    cout << answer << " " << "2" << endl;

    nums = {1, 2};
    answer = solution.minDepth(vectorToTreeNode(nums));
    cout << answer << " " << "2" << endl;

    nums = {};
    answer = solution.minDepth(vectorToTreeNode(nums));
    cout << answer << " " << "0" << endl;

    nums = {1};
    answer = solution.minDepth(vectorToTreeNode(nums));
    cout << answer << " " << "1" << endl;

    nums = {1, 2, 2, 3, 3, -1, -1, 4, 4};
    answer = solution.minDepth(vectorToTreeNode(nums));
    cout << answer << " " << "2" << endl;

    return 0;
}