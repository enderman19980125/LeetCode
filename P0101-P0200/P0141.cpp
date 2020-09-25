#include <iostream>
#include <vector>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;

    explicit ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == nullptr) return false;
        if (head->val == INT_MIN) return true;
        head->val = INT_MIN;
        head = head->next;
        return this->hasCycle(head);
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

    ListNode *head;
    bool answer;

    head = generateLinkedList(vector<int>{3, 2, 0, -4}, 1);
    answer = solution.hasCycle(head);
    cout << to_string(answer) << " " << true << endl;

    head = generateLinkedList(vector<int>{1, 2}, 0);
    answer = solution.hasCycle(head);
    cout << to_string(answer) << " " << true << endl;

    head = generateLinkedList(vector<int>{1}, -1);
    answer = solution.hasCycle(head);
    cout << to_string(answer) << " " << false << endl;

    head = generateLinkedList(vector<int>{1}, 0);
    answer = solution.hasCycle(head);
    cout << to_string(answer) << " " << true << endl;

    head = generateLinkedList(vector<int>{}, 0);
    answer = solution.hasCycle(head);
    cout << to_string(answer) << " " << false << endl;

    head = generateLinkedList(vector<int>{1, 2, 3, 4, 5}, -1);
    answer = solution.hasCycle(head);
    cout << to_string(answer) << " " << false << endl;

    head = generateLinkedList(vector<int>{1, 2, 3, 4, 5}, 0);
    answer = solution.hasCycle(head);
    cout << to_string(answer) << " " << true << endl;

    head = generateLinkedList(vector<int>{1, 2, 3, 4, 5}, 4);
    answer = solution.hasCycle(head);
    cout << to_string(answer) << " " << true << endl;

    return 0;
}