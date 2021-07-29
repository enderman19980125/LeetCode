import heapq
from typing import Tuple, List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = []
        heapq.heappush(heap, 1)
        for prime in primes:
            heapq.heappush(heap, prime)

        k = 0
        while True:
            k += 1
            num = heapq.heappop(heap)
            while heap and num == heap[0]:
                heapq.heappop(heap)
            if k == n:
                return num
            for prime in primes:
                if (next_num := num * prime) <= 2 ** 31:
                    heapq.heappush(heap, next_num)


def test(input_content: Tuple[int, List[int]], std_answer: int) -> None:
    solution = Solution()
    answer = solution.nthSuperUglyNumber(input_content[0], input_content[1])
    print(f"%s %s %s" % (answer == std_answer, answer, std_answer))


if __name__ == '__main__':
    test(input_content=(12, [2, 7, 13, 19]), std_answer=32)
    test(input_content=(1, [2, 3, 5]), std_answer=1)
    test(input_content=(1, [2]), std_answer=1)
    test(input_content=(2, [2]), std_answer=2)
    test(input_content=(4, [2]), std_answer=8)
