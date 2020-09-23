#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
private:
    static int distance(string &word1, string &word2) {
        int d = 0;
        for (int i = 0; i < word1.size(); ++i) {
            if (word1[i] != word2[i]) d++;
            if (d > 1) return d;
        }
        return d;
    }

public:
    int ladderLength(string &beginWord, string &endWord, vector<string> &wordList) {
        wordList.push_back(beginWord);
        int n = wordList.size(), beginWordIndex = n - 1, endWordIndex = -1;
        for (int i = 0; i < n; ++i) if (wordList[i] == endWord) endWordIndex = i;
        if (endWordIndex == -1) return 0;

        vector<int> next[n];
        for (int i = 0; i < n; ++i)
            for (int j = i + 1; j < n; ++j)
                if (Solution::distance(wordList[i], wordList[j]) == 1) {
                    next[i].push_back(j);
                    next[j].push_back(i);
                }

        int dis[n];
        for (int i = 0; i < n; ++i) dis[i] = -1;
        dis[beginWordIndex] = 1;
        queue<int> q;
        q.push(beginWordIndex);
        while (not q.empty()) {
            int i = q.front();
            q.pop();
            for (int j:next[i])
                if (dis[j] == -1 or dis[i] + 1 < dis[j]) {
                    dis[j] = dis[i] + 1;
                    q.push(j);
                }
        }

        return max(0, dis[endWordIndex]);
    }
};

int main() {
    Solution solution = Solution();

    string beginWord, endWord;
    vector<string> wordList;
    int answer;

    beginWord = "hit";
    endWord = "cog";
    wordList = {"hot", "dot", "dog", "lot", "log", "cog"};
    answer = solution.ladderLength(beginWord, endWord, wordList);
    cout << answer << " " << "5" << endl;

    beginWord = "hit";
    endWord = "cog";
    wordList = {"hot", "dot", "dog", "lot", "log"};
    answer = solution.ladderLength(beginWord, endWord, wordList);
    cout << answer << " " << "0" << endl;

    beginWord = "hot";
    endWord = "dog";
    wordList = {"hot", "dog"};
    answer = solution.ladderLength(beginWord, endWord, wordList);
    cout << answer << " " << "0" << endl;

    beginWord = "aa";
    endWord = "bb";
    wordList = {"ab", "ba", "bb"};
    answer = solution.ladderLength(beginWord, endWord, wordList);
    cout << answer << " " << "3" << endl;

    beginWord = "a";
    endWord = "b";
    wordList = {"a", "b"};
    answer = solution.ladderLength(beginWord, endWord, wordList);
    cout << answer << " " << "2" << endl;

    return 0;
}