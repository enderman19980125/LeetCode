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
    int totalSum = 0;

    void search(TreeNode *root, int sum) {
        sum = 10 * sum + root->val;
        if (root->left == nullptr and root->right == nullptr) {
            this->totalSum += sum;
            return;
        }
        if (root->left) this->search(root->left, sum);
        if (root->right) this->search(root->right, sum);
    }

public:
    int sumNumbers(TreeNode *root) {
        if (root == nullptr) return 0;
        this->totalSum = 0;
        this->search(root, 0);
        return totalSum;
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
    answer = solution.sumNumbers(root);
    cout << answer << " " << 25 << endl;

    nums = {4, 9, 0, 5, 1};
    root = vectorToTreeNode(nums);
    answer = solution.sumNumbers(root);
    cout << answer << " " << 1026 << endl;

    nums = {};
    root = vectorToTreeNode(nums);
    answer = solution.sumNumbers(root);
    cout << answer << " " << 0 << endl;

    nums = {1};
    root = vectorToTreeNode(nums);
    answer = solution.sumNumbers(root);
    cout << answer << " " << 1 << endl;

    nums = {1, 2};
    root = vectorToTreeNode(nums);
    answer = solution.sumNumbers(root);
    cout << answer << " " << 12 << endl;

    return 0;
}