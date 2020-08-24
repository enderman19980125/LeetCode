from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if s == "" or words == []:
            return []

        words_dict = {word: words.count(word) for word in set(words)}

        m = len(words[0])
        position_match = []
        for i, _ in enumerate(s):
            for k, word in enumerate(words_dict.keys()):
                if s[i:i + m] == word:
                    position_match.append(word)
                    break
            else:
                position_match.append(-1)

        ans = []
        n_words = len(words)
        for i, _ in enumerate(s):
            match_list = position_match[i:i + n_words * m:m]
            match_dict = {word: match_list.count(word) for word in words_dict.keys()}
            if match_dict == words_dict:
                ans.append(i)

        return ans


if __name__ == '__main__':
    solution = Solution()

    answer = solution.findSubstring("barfoothefoobarman", ["foo", "bar"])
    print(answer, [0, 9])

    answer = solution.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"])
    print(answer, [])

    answer = solution.findSubstring("", [])
    print(answer, [])
