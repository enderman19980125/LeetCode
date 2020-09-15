#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    Node *left;
    Node *right;
    Node *next;

    Node() : val(0), left(nullptr), right(nullptr), next(nullptr) {}

    explicit Node(int _val) : val(_val), left(nullptr), right(nullptr), next(nullptr) {}

    Node(int _val, Node *_left, Node *_right, Node *_next)
            : val(_val), left(_left), right(_right), next(_next) {}
};

class Solution {
private:
    void connectLevel(Node *head) {
        Node *nextLevelPre = nullptr, *nextLevelHead = nullptr;
        while (head) {
            if (head->left) {
                if (nextLevelPre) {
                    nextLevelPre->next = head->left;
                    nextLevelPre = head->left;
                } else {
                    nextLevelPre = head->left;
                }
                if (nextLevelHead == nullptr) nextLevelHead = head->left;
            }
            if (head->right) {
                if (nextLevelPre) {
                    nextLevelPre->next = head->right;
                    nextLevelPre = head->right;
                } else {
                    nextLevelPre = head->right;
                }
                if (nextLevelHead == nullptr) nextLevelHead = head->right;
            }
            head = head->next;
        }
        if (nextLevelHead) this->connectLevel(nextLevelHead);
    }

public:
    Node *connect(Node *root) {
        this->connectLevel(root);
        return root;
    }
};

Node *vectorToNode(vector<int> nodes) {
    if (nodes.empty()) {
        return nullptr;
    }
    queue<Node *> q;
    auto *root_node = new Node(nodes[0]);
    q.push(root_node);
    int k = 1;
    while (k < nodes.size()) {
        Node *root = q.front();
        q.pop();
        if (k < nodes.size()) {
            if (nodes[k] == -1) {
                k++;
            } else {
                auto *left = new Node(nodes[k++]);
                root->left = left;
                q.push(left);
            }
        }
        if (k < nodes.size()) {
            if (nodes[k] == -1) {
                k++;
            } else {
                auto *right = new Node(nodes[k++]);
                root->right = right;
                q.push(right);
            }
        }
    }
    return root_node;
}

string nodesToLevelString(Node *root) {
    vector<Node *> level;
    Node *p = root;
    while (p) {
        level.push_back(p);
        p = p->left;
    }
    vector<int> output;
    for (auto node:level) {
        while (node) {
            output.push_back(node->val);
            node = node->next;
        }
        output.push_back(-1);
    }
    if (output.empty()) output.push_back(-1);
    string output_string;
    for (auto val:output) output_string += (val == -1 ? "#" : to_string(val)) + ", ";
    output_string = "[" + output_string.substr(0, output_string.size() - 2) + "]";
    return output_string;
}

int main() {
    Solution solution = Solution();

    vector<int> nums;
    Node *root;
    Node *answer;

    nums = {1, 2, 3, 4, 5, -1, 7};
    root = vectorToNode(nums);
    answer = solution.connect(root);
    cout << nodesToLevelString(answer) << " " << "[1, #, 2, 3, #, 4, 5, 7, #]" << endl;

    nums = {};
    root = vectorToNode(nums);
    answer = solution.connect(root);
    cout << nodesToLevelString(answer) << " " << "[#]" << endl;

    nums = {1, 2, 3, 4, -1, -1, 7};
    root = vectorToNode(nums);
    answer = solution.connect(root);
    cout << nodesToLevelString(answer) << " " << "[1, #, 2, 3, #, 4, 7, #]" << endl;

    nums = {1, 2, 3, 4, -1, -1, 7, 8, -1};
    root = vectorToNode(nums);
    answer = solution.connect(root);
    cout << nodesToLevelString(answer) << " " << "[1, #, 2, 3, #, 4, 7, #, 8, #]" << endl;

    return 0;
}