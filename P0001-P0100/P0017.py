from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        ans = [""]
        f = {"2": ("a", "b", "c"), "3": ("d", "e", "f"), "4": ("g", "h", "i"), "5": ("j", "k", "l"),
             "6": ("m", "n", "o"), "7": ("p", "q", "r", "s"), "8": ("t", "u", "v"), "9": ("w", "x", "y", "z")}
        for digit in digits:
            new_ans = []
            for v in f[digit]:
                new_ans.extend(map(lambda x: x + v, ans))
            ans = new_ans
        return ans


if __name__ == '__main__':
    solution = Solution()
    answer = solution.letterCombinations("23")
    print(answer)
    print(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
    answer = solution.letterCombinations("")
    print(answer)
    print([])
