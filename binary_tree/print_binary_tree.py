# print binary tree
# every level print one line

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def print_line(l):
    s = []
    for node in l:
        s.append(str(node.val))
    print(",".join(s))


def printbt(head: TreeNode):
    queue = [head]
    next_line = []
    print(head.val)
    while queue or next_line:
        if not queue:
            print_line(next_line)
            queue.extend(next_line)
            next_line = []
        cur = queue.pop(0)
        if cur.left:
            next_line.append(cur.left)
        if cur.right:
            next_line.append(cur.right)


if __name__ == '__main__':
    print('---tase case 1---')
    #     1
    #    / \
    #   2   5
    #  / \
    # 3   4
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.left = node2
    node2.left = node3
    node2.right = node4
    node1.right = node5
    printbt(node1)

    print('---tase case 2---')
    #     6
    node6 = TreeNode(6)
    printbt(node6)
