# restore binary tree
# pre-ord: [1,2,4,7,3,5,6,8]
# tin-ord: [4,7,2,1,5,3,8,6]

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def rebuild(pre: list, tin: list):
    if not pre or not tin:
        return None
    head = TreeNode(pre[0])
    idx_in_tin = tin.index(pre[0])
    if 1 <= idx_in_tin+1 <= len(pre):
        head.left = rebuild(pre[1:idx_in_tin+1], tin[:idx_in_tin])
    if idx_in_tin+1 < len(pre):
        head.right = rebuild(pre[idx_in_tin+1:], tin[idx_in_tin+1:])
    return head

# for print
def print_line(l):
    s = []
    for node in l:
        s.append(str(node.val))
    print(",".join(s))


def printbt(head: TreeNode):
    if not head:
        return
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
    #       1
    #      / \
    #     /   \
    #    2     3
    #   /     / \
    #  4     5   6
    #  |        /
    #  7       8
    pre_ord = [1, 2, 4, 7, 3, 5, 6, 8]
    tin_ord = [4, 7, 2, 1, 5, 3, 8, 6]
    mytree = rebuild(pre_ord, tin_ord)
    printbt(mytree)

    print('---tase case 2---')
    #     1
    pre_ord = [1]
    tin_ord = [1]
    mytree = rebuild(pre_ord, tin_ord)
    printbt(mytree)

    print('---tase case 3---')
    pre_ord = [1, 2, 4, 7]
    tin_ord = [7, 4, 2, 1]
    mytree = rebuild(pre_ord, tin_ord)
    printbt(mytree)
