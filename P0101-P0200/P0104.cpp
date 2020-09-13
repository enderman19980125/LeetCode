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
    int max_depth = 0;

    void search(TreeNode *root, int depth) {
        if (root == nullptr) return;
        if (depth > this->max_depth) this->max_depth = depth;
        search(root->left, depth + 1);
        search(root->right, depth + 1);
    }

public:
    int maxDepth(TreeNode *root) {
        this->max_depth = 0;
        this->search(root, 1);
        return this->max_depth;
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
    int answer;

    nodes = {3, 9, 20, -1, -1, 15, 7};
    root_node = toTree(nodes);
    answer = solution.maxDepth(root_node);
    cout << answer << " " << 3 << endl;

    nodes = {};
    root_node = toTree(nodes);
    answer = solution.maxDepth(root_node);
    cout << answer << " " << 0 << endl;

    nodes = {1};
    root_node = toTree(nodes);
    answer = solution.maxDepth(root_node);
    cout << answer << " " << 1 << endl;

    nodes = {1, -1, 2, 3, -1, 4, 5};
    root_node = toTree(nodes);
    answer = solution.maxDepth(root_node);
    cout << answer << " " << 4 << endl;


    return 0;
}