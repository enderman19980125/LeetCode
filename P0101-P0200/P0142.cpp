#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;

    explicit ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        unordered_set<ListNode *> s;
        while (head) {
            if (s.find(head) != s.end()) return head;
            s.insert(head);
            head = head->next;
        }
        return nullptr;
    }
};

class SolutionTwoPointer {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode *pSlow = head, *pFast = head;
        do {
            if (pSlow == nullptr or pFast == nullptr or pFast->next == nullptr) return nullptr;
            pSlow = pSlow->next;
            pFast = pFast->next->next;
        } while (pSlow != pFast);
        ListNode *p1 = head, *p2 = pSlow;
        while (p1 != p2) p1 = p1->next, p2 = p2->next;
        return p1;
    }
};

ListNode *generateLinkedList(const vector<int> &nums, int pos) {
    if (nums.empty()) return nullptr;
    int n = nums.size();
    ListNode *nodes[n];
    for (int i = 0; i < n; ++i) nodes[i] = new ListNode(nums[i]);
    for (int i = 0; i < n - 1; ++i) nodes[i]->next = nodes[i + 1];
    if (pos != -1) nodes[n - 1]->next = nodes[pos];
    return nodes[0];
}

int main() {
    Solution solution = Solution();

    ListNode *head, *answer;

    head = generateLinkedList(vector<int>{3, 2, 0, -4}, 1);
    answer = solution.detectCycle(head);
    cout << (answer ? answer->val : -1) << " " << 2 << endl;

    head = generateLinkedList(vector<int>{1, 2}, 0);
    answer = solution.detectCycle(head);
    cout << (answer ? answer->val : -1) << " " << 1 << endl;

    head = generateLinkedList(vector<int>{1}, -1);
    answer = solution.detectCycle(head);
    cout << (answer ? answer->val : -1) << " " << -1 << endl;

    head = generateLinkedList(vector<int>{1}, 0);
    answer = solution.detectCycle(head);
    cout << (answer ? answer->val : -1) << " " << 1 << endl;

    head = generateLinkedList(vector<int>{}, 0);
    answer = solution.detectCycle(head);
    cout << (answer ? answer->val : -1) << " " << -1 << endl;

    head = generateLinkedList(vector<int>{1, 2, 3, 4, 5}, -1);
    answer = solution.detectCycle(head);
    cout << (answer ? answer->val : -1) << " " << -1 << endl;

    head = generateLinkedList(vector<int>{1, 2, 3, 4, 5}, 0);
    answer = solution.detectCycle(head);
    cout << (answer ? answer->val : -1) << " " << 1 << endl;

    head = generateLinkedList(vector<int>{1, 2, 3, 4, 5}, 4);
    answer = solution.detectCycle(head);
    cout << (answer ? answer->val : -1) << " " << 5 << endl;

    return 0;
}