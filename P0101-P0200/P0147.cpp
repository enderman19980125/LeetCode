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
    ListNode *insertionSortList(ListNode *head) {
        auto *h = new ListNode(0);
        ListNode *p = head, *pp;

        while (p) {
            ListNode *i = h;
            while (i->next and i->next->val < p->val) i = i->next;
            pp = p->next;
            p->next = i->next;
            i->next = p;
            p = pp;
        }

        return h->next;
    }
};

ListNode *vectorToList(const vector<int> &nums) {
    if (nums.empty()) return nullptr;
    vector<ListNode *> nodes;
    nodes.reserve(nums.size());
    for (const int &num:nums) nodes.emplace_back(new ListNode(num));
    for (int i = 0; i < nodes.size() - 1; ++i) nodes[i]->next = nodes[i + 1];
    return nodes[0];
}

string to_string(ListNode *head) {
    string s = "[";
    while (head) {
        s += to_string(head->val) + ",";
        head = head->next;
    }
    if (s.size() > 1) s = s.substr(0, s.size() - 1);
    s += "]";
    return s;
}

int main() {
    Solution solution = Solution();

    ListNode *head, *answer;

    head = vectorToList(vector<int>{4, 2, 1, 3});
    answer = solution.insertionSortList(head);
    cout << to_string(answer) << " " << "[1,2,3,4]" << endl;

    head = vectorToList(vector<int>{-1, 5, 3, 4, 0});
    answer = solution.insertionSortList(head);
    cout << to_string(answer) << " " << "[-1,0,3,4,5]" << endl;

    head = vectorToList(vector<int>{});
    answer = solution.insertionSortList(head);
    cout << to_string(answer) << " " << "[]" << endl;

    head = vectorToList(vector<int>{1});
    answer = solution.insertionSortList(head);
    cout << to_string(answer) << " " << "[1]" << endl;

    head = vectorToList(vector<int>{2, 1});
    answer = solution.insertionSortList(head);
    cout << to_string(answer) << " " << "[1,2]" << endl;

    head = vectorToList(vector<int>{3, 1, 1});
    answer = solution.insertionSortList(head);
    cout << to_string(answer) << " " << "[1,1,3]" << endl;

    head = vectorToList(vector<int>{3, 1, 1, 2, 2});
    answer = solution.insertionSortList(head);
    cout << to_string(answer) << " " << "[1,1,2,2,3]" << endl;

    head = vectorToList(vector<int>{5, 4, 3, 2, 1});
    answer = solution.insertionSortList(head);
    cout << to_string(answer) << " " << "[1,2,3,4,5]" << endl;

    head = vectorToList(vector<int>{3, 1, 2, 5, 4});
    answer = solution.insertionSortList(head);
    cout << to_string(answer) << " " << "[1,2,3,4,5]" << endl;

    return 0;
}