#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

class LRUCacheTimeBased {
private:
    int capacity = 0, sizeKeys = 0, cntTime = 0;
    queue<int> timeQueue;
    unordered_map<int, int> keyOfTime, numKey, valueOf;

public:
    explicit LRUCacheTimeBased(int capacity) {
        this->capacity = capacity;
        this->sizeKeys = 0;
        this->cntTime = 0;
        this->keyOfTime.clear();
        this->numKey.clear();
        this->valueOf.clear();
        while (not this->timeQueue.empty()) this->timeQueue.pop();
    }

    int get(int key) {
        if (numKey.find(key) == numKey.end() or numKey[key] == 0) return -1;
        timeQueue.emplace(++cntTime);
        keyOfTime[cntTime] = key;
        numKey[key]++;
        return valueOf[key];
    }

    void put(int key, int value) {
        valueOf[key] = value;
        timeQueue.emplace(++cntTime);
        keyOfTime[cntTime] = key;
        numKey[key]++;
        if (numKey[key] == 1) sizeKeys++;
        while (sizeKeys > capacity) {
            int t = timeQueue.front();
            timeQueue.pop();
            int k = keyOfTime[t];
            numKey[k]--;
            if (numKey[k] == 0) sizeKeys--;
        }
    }
};

class LRUCache {
private:
    struct Node {
        int key, value;
        Node *left, *right;

        Node() : value(0), key(0), left(nullptr), right(nullptr) {}

        explicit Node(int key, int value) : key(key), value(value), left(nullptr), right(nullptr) {}
    };

    void move_front(Node *node) {
        Node *leftNode = node->left, *rightNode = node->right;
        leftNode->right = rightNode, rightNode->left = leftNode;
        Node *firstNode = head->right;
        head->right = node, node->right = firstNode;
        node->left = head, firstNode->left = node;
    }

    void insert_front(Node *node) {
        Node *firstNode = head->right;
        head->right = node, node->right = firstNode;
        node->left = head, firstNode->left = node;
    }

    int erase_back() {
        Node *node = tail->left;
        Node *leftNode = node->left, *rightNode = node->right;
        leftNode->right = rightNode, rightNode->left = leftNode;
        int key = node->key;
        delete node;
        return key;
    }

    int capacity = 0;
    Node *head = new Node(-1, -1), *tail = new Node(-1, -1);
    unordered_map<int, Node *> hashMap;

public:
    explicit LRUCache(int capacity) {
        this->capacity = capacity;
        head->right = tail, tail->left = head;
        this->hashMap.clear();
    }

    int get(int key) {
        if (hashMap.find(key) == hashMap.end()) return -1;
        move_front(hashMap[key]);
        return hashMap[key]->value;
    }

    void put(int key, int value) {
        if (hashMap.find(key) == hashMap.end()) {
            hashMap[key] = new Node(key, value);
            insert_front(hashMap[key]);
        } else {
            hashMap[key]->value = value;
            move_front(hashMap[key]);
        }
        while (hashMap.size() > capacity) {
            int k = erase_back();
            hashMap.erase(k);
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,valueOf);
 */

int main() {
    LRUCache cache(0);
    vector<string> operateList;
    vector<vector<int>> numsList;

    operateList = {"LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"};
    numsList = {{2},
                {1, 1},
                {2, 2},
                {1},
                {3, 3},
                {2},
                {4, 4},
                {1},
                {3},
                {4}};
    cache = LRUCache(numsList[0][0]);
    for (int i = 1; i < operateList.size(); ++i) {
        if (operateList[i] == "put")
            cache.put(numsList[i][0], numsList[i][1]);
        else
            cout << cache.get(numsList[i][0]) << " ";
    }
    cout << endl << "1 -1 -1 3 4" << endl << endl;

    operateList = {"LRUCache", "get", "put", "get", "put", "put", "get", "get"};
    numsList = {{2},
                {2},
                {2, 6},
                {1},
                {1, 5},
                {1, 2},
                {1},
                {2}};
    cache = LRUCache(numsList[0][0]);
    for (int i = 1; i < operateList.size(); ++i) {
        if (operateList[i] == "put")
            cache.put(numsList[i][0], numsList[i][1]);
        else
            cout << cache.get(numsList[i][0]) << " ";
    }
    cout << endl << "-1 -1 2 6" << endl << endl;

    return 0;
}