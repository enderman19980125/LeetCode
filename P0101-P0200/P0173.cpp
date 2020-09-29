#include <iostream>
#include <vector>
#include <queue>
#include <stack>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    explicit TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class BSTIterator {
private:
    stack<TreeNode *> stack;
public:
    explicit BSTIterator(TreeNode *root) {
        while (root) {
            stack.push(root);
            root = root->left;
        }
    }

    /** @return the next smallest number */
    int next() {
        TreeNode *cntNode = stack.top();
        stack.pop();
        if (cntNode->right) {
            TreeNode *p = cntNode->right;
            while (p) {
                stack.push(p);
                p = p->left;
            }
        }
        return cntNode->val;
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return not stack.empty();
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */

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

string test(TreeNode *root, vector<string> &operateList) {
    string s = "[";
    auto BST = BSTIterator(root);
    for (string &operate:operateList) {
        if (operate == "next") s += to_string(BST.next());
        if (operate == "hasNext") s += BST.hasNext() ? "true" : "false";
        s += ",";
    }
    if (s.size() > 1) s = s.substr(0, s.size() - 1);
    s += "]";
    return s;
}

int main() {
    vector<int> numsList;
    vector<string> operateList;
    TreeNode *root;
    string answer;

    numsList = {7, 3, 15, INT_MIN, INT_MIN, 9, 20};
    operateList = {"next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"};
    root = vectorToTreeNode(numsList);
    answer = test(root, operateList);
    cout << answer << " " << "[3,7,true,9,true,15,true,20,false]" << endl;

    numsList = {};
    operateList = {"hasNext"};
    root = vectorToTreeNode(numsList);
    answer = test(root, operateList);
    cout << answer << " " << "[false]" << endl;

    numsList = {1};
    operateList = {"hasNext", "next", "hasNext"};
    root = vectorToTreeNode(numsList);
    answer = test(root, operateList);
    cout << answer << " " << "[true,1,false]" << endl;

    numsList = {6, 3, 8, 2, 4, 7, 9, 1, INT_MIN, INT_MIN, 5};
    operateList = {"next", "next", "next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext"};
    root = vectorToTreeNode(numsList);
    answer = test(root, operateList);
    cout << answer << " " << "[1,2,3,4,5,6,7,8,true,9,false]" << endl;

    return 0;
}