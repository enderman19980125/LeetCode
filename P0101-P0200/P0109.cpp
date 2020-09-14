#include <iostream>
#include <queue>
#include <vector>

using namespace std;

//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;

    ListNode() : val(0), next(nullptr) {}

    explicit ListNode(int x) : val(x), next(nullptr) {}

    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    explicit TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
private:
    TreeNode *sortedVectorToBST(vector<int> &nums) {
        if (nums.empty()) return nullptr;
        unsigned int mid_pos = nums.size() / 2;
        auto *root = new TreeNode(nums[mid_pos]);
        vector<int> left_nums(nums.begin(), nums.begin() + mid_pos);
        vector<int> right_nums(nums.begin() + mid_pos + 1, nums.end());
        root->left = this->sortedVectorToBST(left_nums);
        root->right = this->sortedVectorToBST(right_nums);
        return root;
    }

public:
    TreeNode *sortedListToBST(ListNode *head) {
        vector<int> nodes;
        auto *p = head;
        while (p) {
            nodes.push_back(p->val);
            p = p->next;
        }
        return this->sortedVectorToBST(nodes);
    }
};

ListNode *vectorToListNode(vector<int> &nums) {
    if (nums.empty()) return nullptr;
    auto *head = new ListNode();
    auto *pre = head;
    for (auto num:nums) {
        auto p = new ListNode(num);
        pre->next = p;
        pre = p;
    }
    head = head->next;
    return head;
}

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

    vector<int> nums;
    TreeNode *answer;

    nums = {-10, -3, 0, 5, 9};
    answer = solution.sortedListToBST(vectorToListNode(nums));
    cout << treeNodeToString(answer) << " " << "[0, -3, 9, -10, -1, 5]" << endl;

    nums = {};
    answer = solution.sortedListToBST(vectorToListNode(nums));
    cout << treeNodeToString(answer) << " " << "[]" << endl;

    nums = {0};
    answer = solution.sortedListToBST(vectorToListNode(nums));
    cout << treeNodeToString(answer) << " " << "[0]" << endl;

    nums = {1, 3};
    answer = solution.sortedListToBST(vectorToListNode(nums));
    cout << treeNodeToString(answer) << " " << "[3, 1]" << endl;

    nums = {1, 2, 3, 4, 5, 6};
    answer = solution.sortedListToBST(vectorToListNode(nums));
    cout << treeNodeToString(answer) << " " << "[4, 2, 6, 1, 3, 5]" << endl;

    return 0;
}