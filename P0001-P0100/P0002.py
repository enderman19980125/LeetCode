# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(None)
        flag = 0
        p0, p1, p2 = ans, l1, l2
        while p1 is not None or p2 is not None:
            value = (p1.val if p1 is not None else 0) + (p2.val if p2 is not None else 0) + flag
            flag = int(value >= 10)
            p0.next = ListNode(value % 10)
            p0 = p0.next
            p1 = p1.next if p1 is not None else None
            p2 = p2.next if p2 is not None else None
        if flag > 0:
            p0.next = ListNode(flag)
        ans = ans.next
        return ans


if __name__ == '__main__':
    M1 = ListNode(2)
    M2 = ListNode(4)
    M3 = ListNode(3)
    M1.next = M2
    M2.next = M3

    N1 = ListNode(5)
    N2 = ListNode(6)
    N3 = ListNode(4)
    N1.next = N2
    N2.next = N3

    solution = Solution()
    answer = solution.addTwoNumbers(M1, N1)
    while answer is not None:
        print(answer.val, end=" -> " if answer.next else " ")
        answer = answer.next
    print("7 -> 0 -> 8")
