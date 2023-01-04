
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_unival_subtrees(root: TreeNode) -> int:
    if not root:
        return 0

    left_count = count_unival_subtrees(root.left)
    right_count = count_unival_subtrees(root.right)

    if is_unival(root):
        return 1 + left_count + right_count
    else:
        return left_count + right_count

def is_unival(root: TreeNode) -> bool:
    if not root:
        return True

    if root.left and root.left.val != root.val:
        return False
    if root.right and root.right.val != root.val:
        return False

    return is_unival(root.left) and is_unival(root.right)
