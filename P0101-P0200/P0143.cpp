#include <iostream>
#include <vector>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;

    ListNode() : val(0), next(nullptr) {}

    explicit ListNode(int x) : val(x), next(nullptr) {}

    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    void reorderList(ListNode *head) {
        if (head == nullptr) return;

        vector<ListNode *> nodes;
        ListNode *p = head;
        while (p) {
            nodes.emplace_back(p);
            p = p->next;
        }

        int i = 0, j = int(nodes.size()) - 1;
        while (i < j) {
            nodes[i]->next = nodes[j];
            i++;
            if (i != j) nodes[j]->next = nodes[i];
            j--;
        }
        nodes[i]->next = nullptr;
    }
};

ListNode *generateLinkedList(const vector<int> &nums) {
    if (nums.empty()) return nullptr;
    int n = nums.size();
    ListNode *nodes[n];
    for (int i = 0; i < n; ++i) nodes[i] = new ListNode(nums[i]);
    for (int i = 0; i < n - 1; ++i) nodes[i]->next = nodes[i + 1];
    return nodes[0];
}

string to_string(ListNode *head) {
    string s;
    bool isEmpty = head == nullptr;
    while (head) {
        s += to_string(head->val) + "->";
        head = head->next;
    }
    if (not isEmpty) s = s.substr(0, s.size() - 2);
    return s;
}

int main() {
    Solution solution = Solution();

    ListNode *head;

    head = generateLinkedList(vector<int>{});
    solution.reorderList(head);
    cout << to_string(head) << " " << "" << endl;

    head = generateLinkedList(vector<int>{1});
    solution.reorderList(head);
    cout << to_string(head) << " " << "1" << endl;

    head = generateLinkedList(vector<int>{1, 2});
    solution.reorderList(head);
    cout << to_string(head) << " " << "1->2" << endl;

    head = generateLinkedList(vector<int>{1, 2, 3});
    solution.reorderList(head);
    cout << to_string(head) << " " << "1->3->2" << endl;

    head = generateLinkedList(vector<int>{1, 2, 3, 4});
    solution.reorderList(head);
    cout << to_string(head) << " " << "1->4->2->3" << endl;

    head = generateLinkedList(vector<int>{1, 2, 3, 4, 5});
    solution.reorderList(head);
    cout << to_string(head) << " " << "1->5->2->4->3" << endl;

    return 0;
}