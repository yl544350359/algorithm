# print binary tree in zigzag

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
    if not head:
        return
    queue = [head]
    ans = [head]
    next_line = []
    flag = True
    while queue or next_line:
        if not queue:
            queue.extend(next_line)
            if flag:
                next_line.reverse()
                flag = False
            else:
                flag = True
            ans += next_line
            next_line = []
        cur = queue.pop(0)
        if cur.left:
            next_line.append(cur.left)
        if cur.right:
            next_line.append(cur.right)
    print_line(ans)


if __name__ == '__main__':
    print('---tase case 1---')
    #     1
    #    / \
    #   2   5
    #  / \   \
    # 3   4   7
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node7 = TreeNode(7)
    node1.left = node2
    node2.left = node3
    node2.right = node4
    node1.right = node5
    node5.right = node7
    printbt(node1)

    print('---tase case 2---')
    #     6
    node6 = TreeNode(6)
    printbt(node6)

    print('---tase case 3---')
    printbt(None)
