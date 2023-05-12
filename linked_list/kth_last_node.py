# find the kth last node in linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def kth_last_node(head, k):
    length = 0
    if not head:
        return None
    rev = None
    cur = head
    while cur:
        tmp = cur.next
        cur.next = rev
        rev = cur
        cur = tmp
        length += 1
    if length < k:
        return None
    point = rev
    while k-1:
        point = point.next
        k -= 1
    return point.val


if __name__ == '__main__':
    print('---tase case 1---')
    # 1--2--3--4--5
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print(kth_last_node(node1, 1))

    print('---tase case 2---')
    # 1--2--3--4--5
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print(kth_last_node(node1, 5))

    print('---tase case 3---')
    # 1--2--3--4--5
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print(kth_last_node(node1, 6))

    print('---tase case 4---')
    print(kth_last_node(None, 6))
