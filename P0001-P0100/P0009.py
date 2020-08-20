class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        xx, y = x, 0
        while xx != 0:
            y = 10 * y + xx % 10
            xx //= 10
        return x == y


if __name__ == '__main__':
    solution = Solution()
    answer = solution.isPalindrome(121)
    print(answer, True)
    answer = solution.isPalindrome(-121)
    print(answer, False)
    answer = solution.isPalindrome(10)
    print(answer, False)
    answer = solution.isPalindrome(0)
    print(answer, True)
