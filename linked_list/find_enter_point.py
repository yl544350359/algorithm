# find the enter point in loop for linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def find_enter_point(head):
    fast, slow = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            slow2 = head
            while slow.next:
                if slow == slow2:
                    return slow.val
                slow2 = slow2.next
                slow = slow.next

    return None


if __name__ == '__main__':
    print('---tase case 1---')
    # 1--2--3--4--5
    #    |        |
    #    +--------+
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2
    print(find_enter_point(node1))

    print('---tase case 2---')
    # 1--2--3--4--5
    # |           |
    # +-----------+
    node5.next = node1
    print(find_enter_point(node1))

    print('---tase case 3---')
    # 1--2--3--4--5
    node5.next = None
    print(find_enter_point(node1))
