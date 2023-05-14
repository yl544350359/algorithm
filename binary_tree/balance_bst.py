class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def balanceBST( root: TreeNode) -> TreeNode:
    def dfs(root):
        if not root:
            return []
        return dfs(root.left)+ [root] + dfs(root.right)

    def rebuild(arr):
        if not arr:
            return None
        mid=len(arr)//2
        head=arr[mid]
        if mid>0:
            head.left=rebuild(arr[:mid])
        else:
            head.left=None
        if mid<len(arr)-1:
            head.right=rebuild(arr[mid+1:])
        else:
            head.right=None
        return head

    node_list=dfs(root)
    head=rebuild(node_list)
    return head
