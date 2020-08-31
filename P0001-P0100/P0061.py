# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        p = self
        nodes = []
        while p:
            nodes.append(str(p.val))
            p = p.next
        s = " -> ".join(nodes)
        return s


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        n = 0
        p = head
        tail = p
        while p:
            n += 1
            tail = p
            p = p.next

        k = n - k % n + 1
        new_tail, new_head = head, head
        for _ in range(k - 1):
            new_tail = new_head
            new_head = new_head.next
        new_head = new_head if new_head else head

        tail.next = head
        new_tail.next = None

        return new_head


def to_string(head: ListNode) -> str:
    nodes = []
    while head:
        nodes.append(str(head.val))
        head = head.next
    nodes.append("NULL")
    s = "->".join(nodes)
    return s


if __name__ == '__main__':
    n0 = ListNode(0)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)

    solution = Solution()

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = None
    answer = solution.rotateRight(n1, 2)
    print(to_string(answer), "4->5->1->2->3->NULL")

    n0.next = n1
    n1.next = n2
    n2.next = None
    answer = solution.rotateRight(n0, 4)
    print(to_string(answer), "2->0->1->NULL")

    n1.next = None
    answer = solution.rotateRight(n1, 1)
    print(to_string(answer), "1->NULL")

    n1.next = None
    answer = solution.rotateRight(n1, 5)
    print(to_string(answer), "1->NULL")

    n1.next = n2
    n2.next = None
    answer = solution.rotateRight(n1, 1)
    print(to_string(answer), "2->1->NULL")

    n1.next = n2
    n2.next = None
    answer = solution.rotateRight(n1, 2)
    print(to_string(answer), "1->2->NULL")

    n1.next = n2
    n2.next = None
    answer = solution.rotateRight(n1, 4)
    print(to_string(answer), "1->2->NULL")

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = None
    answer = solution.rotateRight(n1, 4)
    print(to_string(answer), "2->3->4->5->1->NULL")

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = None
    answer = solution.rotateRight(n1, 5)
    print(to_string(answer), "1->2->3->4->5->NULL")

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = None
    answer = solution.rotateRight(n1, 8)
    print(to_string(answer), "3->4->5->1->2->NULL")
