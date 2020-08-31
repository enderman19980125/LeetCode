from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        tex = []
        while words:
            i = -1
            length_words = 0
            while i + 1 < len(words) and length_words + len(words[i + 1]) + i + 1 <= maxWidth:
                i += 1
                length_words += len(words[i])
            row_words = words[:i + 1]
            words = words[i + 1:]

            length_space = maxWidth - length_words
            if len(row_words) > 1 and words:
                length_space_per = length_space // (len(row_words) - 1)
                row_space = [length_space_per for _ in row_words[1:]]
                length_space = length_space - length_space_per * len(row_space)
                for i in range(length_space):
                    row_space[i] += 1
                row_space.append(0)
            elif len(row_words) > 1:
                row_space = [1 for _ in row_words[1:]]
                length_space -= len(row_words[1:])
                row_space.append(length_space)
            else:
                row_space = [length_space]

            row = ""
            for word, n_space in zip(row_words, row_space):
                row += word + " " * n_space
            tex.append(row)

        return tex


if __name__ == '__main__':
    solution = Solution()

    std = ["This    is    an",
           "example  of text",
           "justification.  "]
    answer = solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
    print(answer == std)
    print(answer)
    print(std)

    std = ["What   must   be",
           "acknowledgment  ",
           "shall be        "]
    answer = solution.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16)
    print(answer == std)
    print(answer)
    print(std)

    std = ["Science  is  what we",
           "understand      well",
           "enough to explain to",
           "a  computer.  Art is",
           "everything  else  we",
           "do                  "]
    answer = solution.fullJustify(["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
                                   "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20)
    print(answer == std)
    print(answer)
    print(std)
