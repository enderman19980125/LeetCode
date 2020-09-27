#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

struct Point {
    long long x, y;

    Point(long long x, long long y) {
        this->x = x;
        this->y = y;
    }

    bool operator==(const Point &point) const {
        return this->x == point.x and this->y == point.y;
    }
};

struct hash_point {
    size_t operator()(const Point &point) const {
        return hash<long long>()(point.x) ^ hash<long long>()(point.y);
    }
};

struct Line {
    long long a, b, c;

    Line(long long a, long long b, long long c) {
        this->a = a;
        this->b = b;
        this->c = c;
        this->simplify();
        if (this->a < 0) this->a = -this->a, this->b = -this->b, this->c = -this->c;
    }

    bool operator==(const Line &line) const {
        return this->a == line.a and this->b == line.b and this->c == line.c;
    }

    void simplify() {
        long long g = gcd(gcd(abs(a), abs(b)), abs(c));
        if (g == 0) return;
        a /= g, b /= g, c /= g;
    }

    static long long gcd(long long a, long long b) {
        return b == 0 ? a : gcd(b, a % b);
    }
};

struct hash_line {
    size_t operator()(const Line &line) const {
        return hash<long long>()(line.a) ^ hash<long long>()(line.b) ^ hash<long long>()(line.c);
    }
};

class Solution {
public:
    int maxPoints(vector<vector<int>> &points) {
        size_t nPoints = points.size();
        if (nPoints <= 1) return nPoints;

        unordered_map<Point, int, hash_point> uniquePoints;
        for (auto &point:points) {
            auto p = Point(point[0], point[1]);
            if (uniquePoints.find(p) == uniquePoints.end()) uniquePoints[p] = 1; else uniquePoints[p]++;
        }

        unordered_map<Line, int, hash_line> lines;
        for (auto it1 = uniquePoints.begin(); it1 != uniquePoints.end(); ++it1)
            for (auto it2 = it1; it2 != uniquePoints.end(); ++it2) {
                if (it1 == it2) continue;
                auto &p1 = const_cast<Point &>(it1->first), &p2 = const_cast<Point &>(it2->first);
                long long a = p2.y - p1.y, b = p1.x - p2.x, c = p2.x * p1.y - p1.x * p2.y;
                Line l = Line(a, b, c);
                if (lines.find(l) == lines.end()) lines[l] = 0;
            }

        int maxPoints = 0;
        for (auto pObj:uniquePoints) maxPoints = max(maxPoints, pObj.second);
        for (auto &lineObj:lines) {
            Line &l = const_cast<Line &>(lineObj.first);
            for (auto &pObj:uniquePoints) {
                auto &p = const_cast<Point &>(pObj.first);
                if (l.a * p.x + l.b * p.y + l.c == 0) lineObj.second += pObj.second;
            }
            maxPoints = max(maxPoints, lineObj.second);
        }

        return maxPoints;
    }
};

int main() {
    Solution solution = Solution();

    vector<vector<int>> points;
    int answer;

    points = {{1, 1},
              {2, 2},
              {3, 3}};
    answer = solution.maxPoints(points);
    cout << to_string(answer) << " " << 3 << endl;

    points = {{1, 1},
              {3, 2},
              {5, 3},
              {4, 1},
              {2, 3},
              {1, 4}};
    answer = solution.maxPoints(points);
    cout << to_string(answer) << " " << 4 << endl;

    points = {{0, 0},
              {0, 0}};
    answer = solution.maxPoints(points);
    cout << to_string(answer) << " " << 2 << endl;

    points = {{0,     0},
              {1,     65536},
              {65536, 0}};
    answer = solution.maxPoints(points);
    cout << to_string(answer) << " " << 2 << endl;

    points = {{1, 1},
              {1, 1},
              {0, 0},
              {3, 4},
              {4, 5},
              {5, 6},
              {7, 8},
              {8, 9}};
    answer = solution.maxPoints(points);
    cout << to_string(answer) << " " << 5 << endl;

    points = {};
    answer = solution.maxPoints(points);
    cout << to_string(answer) << " " << 0 << endl;

    points = {{1, 1}};
    answer = solution.maxPoints(points);
    cout << to_string(answer) << " " << 1 << endl;

    points = {{1, 1},
              {2, 2}};
    answer = solution.maxPoints(points);
    cout << to_string(answer) << " " << 2 << endl;

    return 0;
}