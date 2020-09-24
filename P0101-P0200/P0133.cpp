#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node *> neighbors;

    Node() {
        val = 0;
        neighbors = vector<Node *>();
    }

    explicit Node(int _val) {
        val = _val;
        neighbors = vector<Node *>();
    }

    Node(int _val, vector<Node *> _neighbors) {
        val = _val;
        neighbors = move(_neighbors);
    }
};

class Solution {
public:
    Node *cloneGraph(Node *node) {
        if (node == nullptr) return nullptr;
        Node *nodes[100];
        for (int i = 1; i <= 100; ++i) nodes[i - 1] = new Node(i);
        queue<Node *> q;
        q.push(node);
        while (not q.empty()) {
            Node *oldNode = q.front();
            Node *newNode = nodes[oldNode->val - 1];
            q.pop();
            if (not newNode->neighbors.empty()) continue;
            for (Node *oldAdjNode:oldNode->neighbors) {
                Node *newAdjNode = nodes[oldAdjNode->val - 1];
                newNode->neighbors.push_back(newAdjNode);
                if (newAdjNode->neighbors.empty()) q.push(oldAdjNode);
            }
        }
        return nodes[0];
    }
};

Node *toGraph(vector<vector<int>> &graph) {
    if (graph.empty()) return nullptr;
    int n = graph.size();
    vector<Node *> nodes(n);
    for (int i = 0; i < n; ++i) nodes[i] = new Node(INT_MIN);
    for (int i = 1; i <= n; ++i) {
        nodes[i - 1]->val = i;
        for (int j:graph[i - 1]) nodes[i - 1]->neighbors.push_back(nodes[j - 1]);
    }
    return nodes[0];
}

string to_string(Node *firstNode) {
    if (firstNode == nullptr) return "[]";
    vector<Node *> nodes(100);
    for (int i = 0; i < 100; ++i) nodes[i] = new Node(INT_MIN);

    queue<Node *> q;
    q.push(firstNode);
    while (not q.empty()) {
        Node *node = q.front();
        q.pop();
        nodes[node->val - 1] = node;
        for (Node *m:node->neighbors) if (nodes[m->val - 1]->val == INT_MIN) q.push(m);
    }

    string s = "[";
    for (Node *node:nodes) {
        if (node->val == INT_MIN) break;
        s += "[";
        for (Node *m:node->neighbors) s += to_string(m->val) + ",";
        if (not node->neighbors.empty()) s = s.substr(0, s.size() - 1);
        s += "],";
    }
    if (not nodes.empty()) s = s.substr(0, s.size() - 1);
    s += "]";
    return s;
}

int main() {
    Solution solution = Solution();

    vector<vector<int>> adjacentList;
    Node *firstNode;
    Node *answer;

    adjacentList = {{2, 4},
                    {1, 3},
                    {2, 4},
                    {1, 3}};
    firstNode = toGraph(adjacentList);
    answer = solution.cloneGraph(firstNode);
    cout << to_string(answer) << " " << "[[2,4],[1,3],[2,4],[1,3]]" << endl;

    adjacentList = {{}};
    firstNode = toGraph(adjacentList);
    answer = solution.cloneGraph(firstNode);
    cout << to_string(answer) << " " << "[[]]" << endl;

    adjacentList = {};
    firstNode = toGraph(adjacentList);
    answer = solution.cloneGraph(firstNode);
    cout << to_string(answer) << " " << "[]" << endl;

    adjacentList = {{2},
                    {1}};
    firstNode = toGraph(adjacentList);
    answer = solution.cloneGraph(firstNode);
    cout << to_string(answer) << " " << "[[2],[1]]" << endl;

    return 0;
}