# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f"val = {self.val}    next = {self.next.val if self.next else None}"


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        h = ListNode(0)
        h.next = head
        p0 = h

        while True:
            pk = p0
            flag = False
            for _ in range(k):
                pk = pk.next
                if pk is None:
                    flag = True
                    break
            if flag:
                break

            pk_next = pk.next
            p1 = p0.next
            pi_pre, pi, pi_next = p0, p1, p1.next
            while pi != pk_next:
                pi.next = pi_pre
                pi_pre, pi, pi_next = pi, pi_next, pi_next.next if pi_next else None
            p0.next = pi_pre
            p1.next = pk_next
            p0 = p1

        h = h.next
        return h


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
    n5.next = None

    answer = solution.reverseKGroup(n1, 1)
    nodes_list = []
    while answer is not None:
        nodes_list.append(answer.val)
        answer = answer.next
    nodes = " -> ".join(map(str, nodes_list))
    print(nodes, "1 -> 2 -> 3 -> 4 -> 5")

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = None

    answer = solution.reverseKGroup(n1, 2)
    nodes_list = []
    while answer is not None:
        nodes_list.append(answer.val)
        answer = answer.next
    nodes = " -> ".join(map(str, nodes_list))
    print(nodes, "2 -> 1 -> 4 -> 3 -> 5")

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = None

    answer = solution.reverseKGroup(n1, 3)
    nodes_list = []
    while answer is not None:
        nodes_list.append(answer.val)
        answer = answer.next
    nodes = " -> ".join(map(str, nodes_list))
    print(nodes, "3 -> 2 -> 1 -> 4 -> 5")

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = None

    answer = solution.reverseKGroup(n1, 5)
    nodes_list = []
    while answer is not None:
        nodes_list.append(answer.val)
        answer = answer.next
    nodes = " -> ".join(map(str, nodes_list))
    print(nodes, "5 -> 4 -> 3 -> 2 -> 1")
