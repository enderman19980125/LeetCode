import unittest


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        answer_list = []

        num = {chr(i): 0 for i in range(97, 122 + 1)}
        for c in s:
            num[c] += 1

        for c in s:
            num[c] -= 1
            if c in answer_list:
                continue
            if not answer_list:
                answer_list.append(c)
                continue
            while answer_list and answer_list[-1] > c and num[answer_list[-1]] > 0:
                answer_list.pop()
            answer_list.append(c)

        return ''.join(answer_list)


class TestStringMethods(unittest.TestCase):
    def test_case_1(self):
        solution = Solution()
        answer = solution.removeDuplicateLetters('bcabc')
        self.assertEqual(answer, 'abc')

    def test_case_2(self):
        solution = Solution()
        answer = solution.removeDuplicateLetters('cbacdcbc')
        self.assertEqual(answer, 'acdb')

    def test_case_3(self):
        solution = Solution()
        answer = solution.removeDuplicateLetters('a')
        self.assertEqual(answer, 'a')

    def test_case_4(self):
        solution = Solution()
        answer = solution.removeDuplicateLetters('abacb')
        self.assertEqual(answer, 'abc')

    def test_case_5(self):
        solution = Solution()
        answer = solution.removeDuplicateLetters('aabbaaccbb')
        self.assertEqual(answer, 'abc')

    def test_case_6(self):
        solution = Solution()
        answer = solution.removeDuplicateLetters('aaccbbccaabb')
        self.assertEqual(answer, 'abc')

    def test_case_7(self):
        solution = Solution()
        answer = solution.removeDuplicateLetters('abcdbce')
        self.assertEqual(answer, 'abcde')


if __name__ == '__main__':
    unittest.main()
