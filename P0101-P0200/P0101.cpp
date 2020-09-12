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
    bool isSymmetric(TreeNode *root) {
        if (root == nullptr) {
            return true;
        }
        return isSymmetric(root->left, root->right);
    }

private:
    bool isSymmetric(TreeNode *root_1, TreeNode *root_2) {
        if (root_1 == nullptr and root_2 == nullptr) {
            return true;
        }
        if ((root_1 == nullptr and root_2 != nullptr) or (root_1 != nullptr and root_2 == nullptr)) {
            return false;
        }
        if (root_1->val != root_2->val) {
            return false;
        }
        return isSymmetric(root_1->left, root_2->right) and isSymmetric(root_1->right, root_2->left);
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

int main() {
    Solution solution = Solution();

    vector<int> nodes;
    TreeNode *root_node;
    bool answer;

    nodes = {1, 2, 2, 3, 4, 4, 3};
    root_node = toTree(nodes);
    answer = solution.isSymmetric(root_node);
    cout << answer << " " << true << endl;

    nodes = {1, 2, 2, -1, 3, -1, 3};
    root_node = toTree(nodes);
    answer = solution.isSymmetric(root_node);
    cout << answer << " " << false << endl;

    nodes = {};
    root_node = toTree(nodes);
    answer = solution.isSymmetric(root_node);
    cout << answer << " " << true << endl;

    nodes = {1, 2, 2, 3};
    root_node = toTree(nodes);
    answer = solution.isSymmetric(root_node);
    cout << answer << " " << false << endl;

    nodes = {1, 2, 3};
    root_node = toTree(nodes);
    answer = solution.isSymmetric(root_node);
    cout << answer << " " << false << endl;

    return 0;
}