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
    ListNode *sortList(ListNode *head) {
        auto *h1 = new ListNode(0), *h2 = new ListNode(0), *p1 = h1, *p2 = h2;
        ListNode *p, *pp;

        int minValue = INT_MAX, maxValue = INT_MIN;
        p = head;
        while (p) {
            minValue = min(minValue, p->val);
            maxValue = max(maxValue, p->val);
            p = p->next;
        }

        double midValue = 0.5 * (minValue + maxValue);
        p = head;
        while (p) {
            pp = p->next;
            if (p->val <= midValue)
                p1->next = p, p1 = p1->next, p1->next = nullptr;
            else
                p2->next = p, p2 = p2->next, p2->next = nullptr;
            p = pp;
        }

        if (h1->next and h2->next) {
            h1->next = this->sortList(h1->next);
            h2->next = this->sortList(h2->next);
        }
        p = h1;
        while (p->next) p = p->next;
        p->next = h2->next;

        return h1->next;
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
    answer = solution.sortList(head);
    cout << to_string(answer) << " " << "[1,2,3,4]" << endl;

    head = vectorToList(vector<int>{-1, 5, 3, 4, 0});
    answer = solution.sortList(head);
    cout << to_string(answer) << " " << "[-1,0,3,4,5]" << endl;

    head = vectorToList(vector<int>{});
    answer = solution.sortList(head);
    cout << to_string(answer) << " " << "[]" << endl;

    head = vectorToList(vector<int>{1});
    answer = solution.sortList(head);
    cout << to_string(answer) << " " << "[1]" << endl;

    head = vectorToList(vector<int>{2, 1});
    answer = solution.sortList(head);
    cout << to_string(answer) << " " << "[1,2]" << endl;

    head = vectorToList(vector<int>{1, 1});
    answer = solution.sortList(head);
    cout << to_string(answer) << " " << "[1,1]" << endl;

    head = vectorToList(vector<int>{2, 3, 1});
    answer = solution.sortList(head);
    cout << to_string(answer) << " " << "[1,2,3]" << endl;

    head = vectorToList(vector<int>{2, 1, 1});
    answer = solution.sortList(head);
    cout << to_string(answer) << " " << "[1,1,2]" << endl;

    head = vectorToList(vector<int>{2, 1, 4, 3});
    answer = solution.sortList(head);
    cout << to_string(answer) << " " << "[1,2,3,4]" << endl;

    head = vectorToList(vector<int>{2, 2, 1, 1});
    answer = solution.sortList(head);
    cout << to_string(answer) << " " << "[1,1,2,2]" << endl;

    head = vectorToList(vector<int>{
            -84, 142, 41, -17, -71, 170, 186, 183, -21, -76, 76, 10, 29, 81, 112, -39, -6, -43, 58, 41, 111, 33, 69, 97,
            -38, 82, -44, -7, 99, 135, 42, 150, 149, -21, -30, 164, 153, 92, 180, -61, 99, -81, 147, 109, 34, 98, 14,
            178, 105, 5, 43, 46, 40, -37, 23, 16, 123, -53, 34, 192, -73, 94, 39, 96, 115, 88, -31, -96, 106, 131, 64,
            189, -91, -34, -56, -22, 105, 104, 22, -31, -43, 90, 96, 65, -85, 184, 85, 90, 118, 152, -31, 161, 22, 104,
            -85, 160, 120, -31, 144, 115});
    answer = solution.sortList(head);
    cout << to_string(answer) << endl
         << "[-96,-91,-85,-85,-84,-81,-76,-73,-71,-61,-56,-53,-44,-43,-43,-39,-38,-37,-34,-31,-31,-31,-31,-30,-22,-21,"
            "-21,-17,-7,-6,5,10,14,16,22,22,23,29,33,34,34,39,40,41,41,42,43,46,58,64,65,69,76,81,82,85,88,90,90,92,94,"
            "96,96,97,98,99,99,104,104,105,105,106,109,111,112,115,115,118,120,123,131,135,142,144,147,149,150,152,153,"
            "160,161,164,170,178,180,183,184,186,189,192]"
         << endl;

    return 0;
}