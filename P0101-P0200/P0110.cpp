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
    int balanced(TreeNode *root) {
        if (root == nullptr) return 0;
        int left_height = this->balanced(root->left);
        int right_height = this->balanced(root->right);
        if (left_height >= 0 and right_height >= 0 and abs(left_height - right_height) <= 1) {
            return max(left_height, right_height) + 1;
        } else {
            return -1;
        }
    }

public:
    bool isBalanced(TreeNode *root) {
        if (root == nullptr) return true;
        int left_height = this->balanced(root->left);
        int right_height = this->balanced(root->right);
        return left_height >= 0 and right_height >= 0 and abs(left_height - right_height) <= 1;
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

    nums = {3, 9, 20, -1, -1, 15, 7};
    answer = solution.isBalanced(vectorToTreeNode(nums));
    cout << answer << " " << "1" << endl;

    nums = {1, 2, 2, 3, 3, -1, -1, 4, 4};
    answer = solution.isBalanced(vectorToTreeNode(nums));
    cout << answer << " " << "0" << endl;

    nums = {};
    answer = solution.isBalanced(vectorToTreeNode(nums));
    cout << answer << " " << "1" << endl;

    nums = {1};
    answer = solution.isBalanced(vectorToTreeNode(nums));
    cout << answer << " " << "1" << endl;

    nums = {1, 2};
    answer = solution.isBalanced(vectorToTreeNode(nums));
    cout << answer << " " << "1" << endl;

    nums = {1, 2, 3, 4};
    answer = solution.isBalanced(vectorToTreeNode(nums));
    cout << answer << " " << "1" << endl;

    nums = {1, 2, 3, 4, 5, 6, 7, 8};
    answer = solution.isBalanced(vectorToTreeNode(nums));
    cout << answer << " " << "1" << endl;

    nums = {1, 2, 3, 4, -1, -1, -1, 5};
    answer = solution.isBalanced(vectorToTreeNode(nums));
    cout << answer << " " << "0" << endl;

    return 0;
}