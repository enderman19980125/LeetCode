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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (headA == nullptr or headB == nullptr) return nullptr;
        ListNode *ans = nullptr, *pa = headA, *pb = headB;
        while (pa) {
            pa->val *= -1;
            pa = pa->next;
        }
        while (pb) {
            if (pb->val < 0) {
                ans = pb;
                break;
            }
            pb = pb->next;
        }
        pa = headA;
        while (pa) {
            pa->val *= -1;
            pa = pa->next;
        }
        return ans;
    }
};

pair<ListNode *, ListNode *> generateLinkedList(vector<int> &list1, vector<int> &list2, vector<int> &list12) {
    vector<ListNode *> nodes1, nodes2, nodes12;
    nodes1.emplace_back(new ListNode(0));
    nodes2.emplace_back(new ListNode(0));
    for (int value:list1) nodes1.emplace_back(new ListNode(value));
    for (int value:list2) nodes2.emplace_back(new ListNode(value));
    for (int value:list12) nodes12.emplace_back(new ListNode(value));
    for (int i = 0; i < int(nodes1.size()) - 1; ++i) nodes1[i]->next = nodes1[i + 1];
    for (int i = 0; i < int(nodes2.size()) - 1; ++i) nodes2[i]->next = nodes2[i + 1];
    for (int i = 0; i < int(nodes12.size()) - 1; ++i) nodes12[i]->next = nodes12[i + 1];
    if (not nodes12.empty()) {
        nodes1[nodes1.size() - 1]->next = nodes12[0];
        nodes2[nodes2.size() - 1]->next = nodes12[0];
    }
    pair<ListNode *, ListNode *> heads = {nodes1[0], nodes2[0]};
    return heads;
}

int main() {
    Solution solution = Solution();

    vector<int> list1, list2, list12;
    pair<ListNode *, ListNode *> heads;
    ListNode *answer;

    list1 = {4, 1};
    list2 = {5, 6, 1};
    list12 = {8, 4, 5};
    heads = generateLinkedList(list1, list2, list12);
    answer = solution.getIntersectionNode(heads.first, heads.second);
    cout << (answer ? to_string(answer->val) : "null") << " " << 8 << endl;

    list1 = {1, 9, 1};
    list2 = {3};
    list12 = {2, 4};
    heads = generateLinkedList(list1, list2, list12);
    answer = solution.getIntersectionNode(heads.first, heads.second);
    cout << (answer ? to_string(answer->val) : "null") << " " << 2 << endl;

    list1 = {2, 6, 4};
    list2 = {1, 5};
    list12 = {};
    heads = generateLinkedList(list1, list2, list12);
    answer = solution.getIntersectionNode(heads.first, heads.second);
    cout << (answer ? to_string(answer->val) : "null") << " " << "null" << endl;

    list1 = {};
    list2 = {};
    list12 = {};
    heads = generateLinkedList(list1, list2, list12);
    answer = solution.getIntersectionNode(heads.first, heads.second);
    cout << (answer ? to_string(answer->val) : "null") << " " << "null" << endl;

    list1 = {1};
    list2 = {};
    list12 = {};
    heads = generateLinkedList(list1, list2, list12);
    answer = solution.getIntersectionNode(heads.first, heads.second);
    cout << (answer ? to_string(answer->val) : "null") << " " << "null" << endl;

    list1 = {};
    list2 = {1};
    list12 = {};
    heads = generateLinkedList(list1, list2, list12);
    answer = solution.getIntersectionNode(heads.first, heads.second);
    cout << (answer ? to_string(answer->val) : "null") << " " << "null" << endl;

    list1 = {};
    list2 = {};
    list12 = {1};
    heads = generateLinkedList(list1, list2, list12);
    answer = solution.getIntersectionNode(heads.first, heads.second);
    cout << (answer ? to_string(answer->val) : "null") << " " << 1 << endl;

    list1 = {};
    list2 = {1};
    list12 = {2};
    heads = generateLinkedList(list1, list2, list12);
    answer = solution.getIntersectionNode(heads.first, heads.second);
    cout << (answer ? to_string(answer->val) : "null") << " " << 2 << endl;

    list1 = {1};
    list2 = {};
    list12 = {2};
    heads = generateLinkedList(list1, list2, list12);
    answer = solution.getIntersectionNode(heads.first, heads.second);
    cout << (answer ? to_string(answer->val) : "null") << " " << 2 << endl;

    list1 = {1};
    list2 = {1};
    list12 = {};
    heads = generateLinkedList(list1, list2, list12);
    answer = solution.getIntersectionNode(heads.first, heads.second);
    cout << (answer ? to_string(answer->val) : "null") << " " << "null" << endl;

    list1 = {1};
    list2 = {1};
    list12 = {2};
    heads = generateLinkedList(list1, list2, list12);
    answer = solution.getIntersectionNode(heads.first, heads.second);
    cout << (answer ? to_string(answer->val) : "null") << " " << 2 << endl;

    return 0;
}