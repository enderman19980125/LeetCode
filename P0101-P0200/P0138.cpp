#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    int pos;
    Node *next;
    Node *random;

    explicit Node(int _val) {
        val = _val;
        pos = -1;
        next = nullptr;
        random = nullptr;
    }
};

class Solution {
public:
    Node *copyRandomList(Node *head) {
        if (head == nullptr) return nullptr;
        unordered_map<Node *, Node *> m;

        Node *p = head;
        while (p) {
            Node *pp = new Node(p->val);
            // pp->pos = p->pos;
            m[p] = pp;
            p = p->next;
        }

        p = head;
        while (p) {
            if (p->next) m[p]->next = m[p->next];
            if (p->random) m[p]->random = m[p->random];
            p = p->next;
        }

        return m[head];
    }
};

Node *vectorToNode(vector<vector<int>> &nums) {
    if (nums.empty()) return nullptr;
    int n = nums.size();
    Node *nodes[n];
    for (int i = 0; i < n; ++i) nodes[i] = new Node(0);
    for (int i = 0; i < n; ++i) {
        nodes[i]->val = nums[i][0];
        nodes[i]->pos = i;
        if (nums[i][1] != INT_MIN) nodes[i]->random = nodes[nums[i][1]];
        if (i != n - 1) nodes[i]->next = nodes[i + 1];
    }
    return nodes[0];
}

string to_string(Node *node) {
    vector<Node *> nodes;
    while (node) {
        nodes.push_back(node);
        node = node->next;
    }
    string s = "[";
    for (Node *n:nodes) {
        s += "[" + to_string(n->val) + ",";
        s += n->random ? to_string(n->pos) : "null";
        s += "],";
    }
    if (not nodes.empty()) s = s.substr(0, s.size() - 1);
    s += "]";
    return s;
}

int main() {
    Solution solution = Solution();

    vector<vector<int>> nums;
    Node *head, *answer;

    nums = {{7, INT_MIN},
            {13, 0},
            {11, 4},
            {10, 2},
            {1,  0}};
    head = vectorToNode(nums);
    answer = solution.copyRandomList(head);
    cout << to_string(answer) << " " << to_string(head) << endl;

    nums = {};
    head = vectorToNode(nums);
    answer = solution.copyRandomList(head);
    cout << to_string(answer) << " " << to_string(head) << endl;

    nums = {{1, 0}};
    head = vectorToNode(nums);
    answer = solution.copyRandomList(head);
    cout << to_string(answer) << " " << to_string(head) << endl;

    nums = {{1, 1},
            {2, 0}};
    head = vectorToNode(nums);
    answer = solution.copyRandomList(head);
    cout << to_string(answer) << " " << to_string(head) << endl;

    return 0;
}