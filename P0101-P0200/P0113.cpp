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
    vector<vector<int>> paths;

    void search(TreeNode *root, int sum, vector<int> path) {
        if (root == nullptr) return;
        path.push_back(root->val);
        if (root->left == nullptr and root->right == nullptr) {
            if (root->val == sum) this->paths.push_back(path);
            return;
        }
        this->search(root->left, sum - root->val, path);
        this->search(root->right, sum - root->val, path);
    }

public:
    vector<vector<int>> pathSum(TreeNode *root, int sum) {
        this->paths = {};
        this->search(root, sum, vector<int>{});
        return this->paths;
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

string doubleVectorToString(const vector<vector<int>> &array) {
    string s = "[";
    for (auto &row: array) {
        s += "[";
        for (auto element:row) {
            s += to_string(element) + ", ";
        }
        s = (row.empty() ? s : s.substr(0, s.size() - 2)) + "], ";
    }
    s = (array.empty() ? s : s.substr(0, s.size() - 2)) + "]";
    return s;
}

int main() {
    Solution solution = Solution();

    vector<int> nums;
    vector<vector<int>> answer;

    nums = {5, 4, 8, 11, -1, 13, 4, 7, 2, -1, -1, 5, 1};
    answer = solution.pathSum(vectorToTreeNode(nums), 22);
    cout << doubleVectorToString(answer) << " " << "[[5, 4, 11, 2], [5, 8, 4, 5]]" << endl;

    nums = {};
    answer = solution.pathSum(vectorToTreeNode(nums), 0);
    cout << doubleVectorToString(answer) << " " << "[]" << endl;

    nums = {1};
    answer = solution.pathSum(vectorToTreeNode(nums), 1);
    cout << doubleVectorToString(answer) << " " << "[[1]]" << endl;

    nums = {1, 2, 2};
    answer = solution.pathSum(vectorToTreeNode(nums), 3);
    cout << doubleVectorToString(answer) << " " << "[[1, 2], [1, 2]]" << endl;

    nums = {1, 2, 1, -1, -1, 1, 1};
    answer = solution.pathSum(vectorToTreeNode(nums), 3);
    cout << doubleVectorToString(answer) << " " << "[[1, 2], [1, 1, 1], [1, 1, 1]]" << endl;

    return 0;
}