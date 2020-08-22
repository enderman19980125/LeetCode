# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        h = ListNode(0)
        h.next = head
        p = h

        while p.next and p.next.next:
            p1, p2 = p.next, p.next.next
            p.next = p2
            p1.next = p2.next
            p2.next = p1
            p = p1

        h = h.next
        return h


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    solution = Solution()
    answer = solution.swapPairs(n1)
    nodes_list = []
    while answer is not None:
        nodes_list.append(answer.val)
        answer = answer.next
    nodes = " -> ".join(map(str, nodes_list))
    print(nodes, "2 -> 1 -> 4 -> 3")

    n1.next = n2
    n2.next = n3

    answer = solution.swapPairs(n1)
    nodes_list = []
    while answer is not None:
        nodes_list.append(answer.val)
        answer = answer.next
    nodes = " -> ".join(map(str, nodes_list))
    print(nodes, "2 -> 1 -> 3")

    n1.next = None

    answer = solution.swapPairs(n1)
    nodes_list = []
    while answer is not None:
        nodes_list.append(answer.val)
        answer = answer.next
    nodes = " -> ".join(map(str, nodes_list))
    print(nodes, "1")
