# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodes = []
        p = head
        while p is not None:
            nodes.append(p)
            p = p.next
        m = len(nodes) - n

        if m == 0:
            head = head.next
        elif n == 1:
            nodes[m - 1].next = None
        else:
            nodes[m - 1].next = nodes[m + 1]

        return head


if __name__ == '__main__':
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

    answer = solution.removeNthFromEnd(n1, 2)
    nodes_list = []
    while answer is not None:
        nodes_list.append(answer.val)
        answer = answer.next
    nodes = " -> ".join(map(str, nodes_list))
    print(nodes, "1 -> 2 -> 3 -> 5")

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    answer = solution.removeNthFromEnd(n1, 1)
    nodes_list = []
    while answer is not None:
        nodes_list.append(answer.val)
        answer = answer.next
    nodes_str = " -> ".join(map(str, nodes_list))
    print(nodes_str, "1 -> 2 -> 3 -> 4")

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    answer = solution.removeNthFromEnd(n1, 5)
    nodes_list = []
    while answer is not None:
        nodes_list.append(answer.val)
        answer = answer.next
    nodes_str = " -> ".join(map(str, nodes_list))
    print(nodes_str, "2 -> 3 -> 4 -> 5")
